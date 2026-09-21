#!/usr/bin/env python3
"""In-silico identifiability of organ-graph metastasis under lumped outputs.

Research-only numerical laboratory. Not a medical device, not a patient-data
fit, not a metastasis-treatment claim. Toy five-node anatomy:
primary (P), lung (L), liver (V), bone (B), brain (R).

Reproduces Chapter 4 numbers for Thesis #5.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from numpy.linalg import eigvalsh, matrix_rank, norm, svd
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "results" / "identifiability_results.json"
OUT_MD = ROOT / "results" / "identifiability_tables.md"

NODES = ("P", "L", "V", "B", "R")
N = len(NODES)
P, L, V, B, R = range(N)
RNG = np.random.default_rng(5)
T_END = 40.0
N_OBS = 81
T_OBS = np.linspace(0.0, T_END, N_OBS)
X0 = np.array([1.0, 0.0, 0.0, 0.0, 0.0], dtype=float)


def pack_W(edges: dict[tuple[int, int], float]) -> np.ndarray:
    W = np.zeros((N, N), dtype=float)
    for (src, dst), rate in edges.items():
        W[dst, src] = float(rate)
    return W


def conservative_rhs(t, x, r, K, W):
    x = np.clip(x, 0.0, None)
    out = W.sum(axis=0)
    growth = r * x * (1.0 - x / K)
    return growth + W @ x - out * x


def linear_rhs(t, x, r, W):
    x = np.clip(x, 0.0, None)
    out = W.sum(axis=0)
    return r * x + W @ x - out * x


def simulate(rhs, args, t_obs=T_OBS, x0=X0):
    sol = solve_ivp(
        rhs,
        (t_obs[0], t_obs[-1]),
        x0,
        t_eval=t_obs,
        args=args,
        method="RK45",
        rtol=1e-8,
        atol=1e-10,
        dense_output=False,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y.T  # (T, N)


def lump(X):
    return X.sum(axis=1)


def rmse(a, b):
    return float(np.sqrt(np.mean((a - b) ** 2)))


def max_abs(a, b):
    return float(np.max(np.abs(a - b)))


def first_detectable_site(X, tau=0.05):
    """First node other than primary to cross tau."""
    distant = X[:, 1:]
    hit = distant >= tau
    if not hit.any():
        return None, None
    # time index of first hit anywhere
    any_hit = hit.any(axis=1)
    t_idx = int(np.argmax(any_hit))
    sites = np.where(hit[t_idx])[0]
    # if several cross in same sample, pick the largest
    j = int(sites[np.argmax(distant[t_idx, sites])])
    return NODES[j + 1], float(T_OBS[t_idx])


# ---------------------------------------------------------------------------
# Experiment 1 — linear homogeneous growth: transfers vanish from the lump
# ---------------------------------------------------------------------------
r_lin = 0.08
W_filter = pack_W(
    {
        (P, L): 0.12,
        (L, V): 0.05,
        (L, B): 0.04,
        (L, R): 0.01,
        (V, P): 0.02,  # reseeding of primary
        (B, P): 0.01,
    }
)
W_skip = pack_W(
    {
        (P, V): 0.10,
        (P, B): 0.06,
        (P, L): 0.02,
        (V, R): 0.03,
        (B, L): 0.04,
        (V, P): 0.03,
    }
)

X_lin_ff = simulate(linear_rhs, (r_lin, W_filter))
X_lin_sk = simulate(linear_rhs, (r_lin, W_skip))
y_lin_ff = lump(X_lin_ff)
y_lin_sk = lump(X_lin_sk)
y_closed = X0.sum() * np.exp(r_lin * T_OBS)

exp1 = {
    "r": r_lin,
    "lump_rmse_filter_vs_skip": rmse(y_lin_ff, y_lin_sk),
    "lump_maxabs_filter_vs_skip": max_abs(y_lin_ff, y_lin_sk),
    "lump_rmse_filter_vs_closed_form": rmse(y_lin_ff, y_closed),
    "site_rmse_filter_vs_skip": rmse(X_lin_ff, X_lin_sk),
    "site_maxabs_filter_vs_skip": max_abs(X_lin_ff, X_lin_sk),
    "final_occupancy_filter": {n: float(X_lin_ff[-1, i]) for i, n in enumerate(NODES)},
    "final_occupancy_skip": {n: float(X_lin_sk[-1, i]) for i, n in enumerate(NODES)},
    "first_site_filter": first_detectable_site(X_lin_ff),
    "first_site_skip": first_detectable_site(X_lin_sk),
}


# ---------------------------------------------------------------------------
# Experiment 2 — logistic soil: lump *almost* matches after compensating K,r
# Tune skip-path (r, K, selected edges) to match filter-flow lumped y
# ---------------------------------------------------------------------------
r_ff = np.array([0.18, 0.12, 0.10, 0.11, 0.07])
K_ff = np.array([80.0, 25.0, 40.0, 35.0, 8.0])
W_ff_log = pack_W(
    {
        (P, L): 0.045,
        (L, V): 0.018,
        (L, B): 0.015,
        (L, R): 0.004,
        (V, P): 0.006,
        (B, P): 0.003,
        (L, P): 0.008,  # self-seeding via lung
    }
)
X_ff = simulate(conservative_rhs, (r_ff, K_ff, W_ff_log))
y_ff = lump(X_ff)

# free parameters for skip-path: r (5), K (5), six edge rates
EDGE_KEYS = [(P, V), (P, B), (P, L), (V, R), (B, L), (V, P)]


def unpack_skip(theta):
    r = np.clip(theta[:5], 0.01, 0.6)
    K = np.clip(theta[5:10], 2.0, 200.0)
    W = pack_W({k: max(theta[10 + i], 0.0) for i, k in enumerate(EDGE_KEYS)})
    return r, K, W


def skip_residual(theta):
    r, K, W = unpack_skip(theta)
    X = simulate(conservative_rhs, (r, K, W))
    return lump(X) - y_ff


theta0 = np.array(
    [0.18, 0.10, 0.16, 0.12, 0.08, 80.0, 18.0, 50.0, 30.0, 10.0, 0.04, 0.03, 0.01, 0.01, 0.02, 0.01]
)
fit = least_squares(skip_residual, theta0, xtol=1e-10, ftol=1e-10, max_nfev=200)
r_sk, K_sk, W_sk_log = unpack_skip(fit.x)
X_sk = simulate(conservative_rhs, (r_sk, K_sk, W_sk_log))
y_sk = lump(X_sk)
site_ff, t_ff = first_detectable_site(X_ff)
site_sk, t_sk = first_detectable_site(X_sk)

exp2 = {
    "cost": float(fit.cost),
    "lump_rmse": rmse(y_ff, y_sk),
    "lump_maxabs": max_abs(y_ff, y_sk),
    "rel_lump_rmse": rmse(y_ff, y_sk) / float(np.mean(y_ff)),
    "site_rmse": rmse(X_ff, X_sk),
    "site_maxabs": max_abs(X_ff, X_sk),
    "first_site_filter": {"site": site_ff, "t": t_ff},
    "first_site_skip": {"site": site_sk, "t": t_sk},
    "final_filter": {n: float(X_ff[-1, i]) for i, n in enumerate(NODES)},
    "final_skip": {n: float(X_sk[-1, i]) for i, n in enumerate(NODES)},
    "r_filter": r_ff.tolist(),
    "r_skip": r_sk.tolist(),
    "K_filter": K_ff.tolist(),
    "K_skip": K_sk.tolist(),
    "y_final_filter": float(y_ff[-1]),
    "y_final_skip": float(y_sk[-1]),
    "primary_rmse": rmse(X_ff[:, 0], X_sk[:, 0]),
}


# ---------------------------------------------------------------------------
# Experiment 3 — Fisher information ranks under three observation maps
# Parameters: the six skip-path edge rates around the fitted skip model,
# plus a local growth perturbation of liver vs lung (soil).
# ---------------------------------------------------------------------------
def fim_for_map(theta, simulate_from_theta, obs_fn, sigma=1.0, delta=1e-5):
    y0 = obs_fn(simulate_from_theta(theta))
    p = theta.size
    S = np.zeros((y0.size, p))
    for j in range(p):
        th = theta.copy()
        step = delta * max(abs(th[j]), 1.0)
        th[j] += step
        S[:, j] = (obs_fn(simulate_from_theta(th)) - y0) / step
    F = (S.T @ S) / (sigma ** 2)
    # numerical rank with relative tolerance
    svals = svd(F, compute_uv=False)
    smax = svals[0] if svals.size else 0.0
    rank = int(np.sum(svals > 1e-8 * max(smax, 1e-30)))
    # sloppy ratio: largest / smallest positive
    pos = svals[svals > 1e-12]
    sloppy = float(pos[0] / pos[-1]) if pos.size else float("inf")
    return {
        "eigs": [float(v) for v in svals],
        "rank": rank,
        "n_params": int(p),
        "n_obs": int(y0.size),
        "log10_condition_pos": float(np.log10(sloppy)) if np.isfinite(sloppy) else None,
        "min_pos_eig": float(pos[-1]) if pos.size else 0.0,
        "max_eig": float(svals[0]) if svals.size else 0.0,
        "sensitivity_col_norms": [float(norm(S[:, j])) for j in range(p)],
    }


theta_edges = np.array([W_sk_log[dst, src] for src, dst in EDGE_KEYS], dtype=float)


def sim_edges(th):
    W = pack_W({k: max(th[i], 0.0) for i, k in enumerate(EDGE_KEYS)})
    return simulate(conservative_rhs, (r_sk, K_sk, W))


def obs_lump(X):
    return lump(X)


def obs_primary(X):
    return X[:, 0]


def obs_full(X):
    return X.ravel()


def obs_count(X, tau=0.05):
    return (X >= tau).sum(axis=1).astype(float)


fim_lump = fim_for_map(theta_edges, sim_edges, obs_lump)
fim_primary = fim_for_map(theta_edges, sim_edges, obs_primary)
fim_full = fim_for_map(theta_edges, sim_edges, obs_full)
fim_count = fim_for_map(theta_edges, sim_edges, obs_count)

exp3 = {
    "edge_names": [f"{NODES[s]}->{NODES[d]}" for s, d in EDGE_KEYS],
    "theta_edges": theta_edges.tolist(),
    "fim_lump": fim_lump,
    "fim_primary": fim_primary,
    "fim_full": fim_full,
    "fim_count": fim_count,
}


# ---------------------------------------------------------------------------
# Experiment 4 — profile of two routes that trade under the lump
# Hold total primary shedding fixed: a = W_P→L, b = W_P→V, a+b = c
# ---------------------------------------------------------------------------
c_shed = 0.05
alphas = np.linspace(0.0, 1.0, 21)
profile = []
X_ref = simulate(
    conservative_rhs,
    (r_ff, K_ff, pack_W({(P, L): c_shed, (L, V): 0.018, (L, B): 0.015})),
)
y_ref = lump(X_ref)
for a in alphas:
    W = pack_W({(P, L): c_shed * a, (P, V): c_shed * (1.0 - a), (L, V): 0.018, (L, B): 0.015})
    X = simulate(conservative_rhs, (r_ff, K_ff, W))
    profile.append(
        {
            "alpha_lung_share": float(a),
            "lump_sse": float(np.sum((lump(X) - y_ref) ** 2)),
            "site_sse": float(np.sum((X - X_ref) ** 2)),
            "first_site": first_detectable_site(X)[0],
            "liver_final": float(X[-1, V]),
            "lung_final": float(X[-1, L]),
        }
    )

exp4 = {
    "c_shed": c_shed,
    "profile": profile,
    "lump_sse_range": [min(p["lump_sse"] for p in profile), max(p["lump_sse"] for p in profile)],
    "site_sse_range": [min(p["site_sse"] for p in profile), max(p["site_sse"] for p in profile)],
}


# ---------------------------------------------------------------------------
# Experiment 5 — binary occupancy CTMC: first-event time vs first-site identity
# Filter-flow rates vs skip rates, matched mean first-event time by scaling.
# ---------------------------------------------------------------------------
def occupancy_first_events(rate_from_primary, n_paths=4000, t_max=80.0):
    """rate_from_primary: dict dest -> rate from occupied primary.
    Distant nodes: L,V,B,R. Independent competing exponentials from P.
    After first hit, process stops for this statistic.
    """
    dests = np.array([L, V, B, R])
    rates = np.array([rate_from_primary[d] for d in dests], dtype=float)
    total = rates.sum()
    # waiting time ~ Exp(total); site ~ categorical(rates)
    waits = RNG.exponential(1.0 / total, size=n_paths)
    waits = np.minimum(waits, t_max)
    sites = RNG.choice(dests, size=n_paths, p=rates / total)
    timed_out = waits >= t_max
    return waits, sites, timed_out, dests, rates


# Two anatomies with the SAME total primary shedding (same first-event law)
# but different site identity.
rate_ff = {L: 0.08, V: 0.005, B: 0.01, R: 0.005}  # lung-first filter
rate_sk = {L: 0.02, V: 0.06, B: 0.015, R: 0.005}  # liver-heavy skip
# equalise total rate
s_ff, s_sk = sum(rate_ff.values()), sum(rate_sk.values())
rate_sk = {k: v * s_ff / s_sk for k, v in rate_sk.items()}

w_ff, s_ff_ids, to_ff, dests, _ = occupancy_first_events(rate_ff)
w_sk, s_sk_ids, to_sk, _, _ = occupancy_first_events(rate_sk)


def site_hist(ids):
    h = {NODES[i]: int(np.sum(ids == i)) for i in (L, V, B, R)}
    return h


def ks_times(a, b):
    # two-sample KS statistic (no scipy.stats dependency beyond numpy)
    a = np.sort(a)
    b = np.sort(b)
    pts = np.concatenate([a, b])
    cdf_a = np.searchsorted(a, pts, side="right") / a.size
    cdf_b = np.searchsorted(b, pts, side="right") / b.size
    return float(np.max(np.abs(cdf_a - cdf_b)))


exp5 = {
    "n_paths": 4000,
    "mean_wait_filter": float(w_ff.mean()),
    "mean_wait_skip": float(w_sk.mean()),
    "median_wait_filter": float(np.median(w_ff)),
    "median_wait_skip": float(np.median(w_sk)),
    "ks_waiting_times": ks_times(w_ff, w_sk),
    "site_hist_filter": site_hist(s_ff_ids),
    "site_hist_skip": site_hist(s_sk_ids),
    "first_site_mode_filter": NODES[int(np.bincount(s_ff_ids, minlength=N).argmax())],
    "first_site_mode_skip": NODES[int(np.bincount(s_sk_ids, minlength=N).argmax())],
    "rate_filter": {NODES[k]: float(v) for k, v in rate_ff.items()},
    "rate_skip": {NODES[k]: float(v) for k, v in rate_sk.items()},
}


# ---------------------------------------------------------------------------
# Experiment 6 — spreader/sponge from a toy transition matrix; undefined on T(t)
# ---------------------------------------------------------------------------
# Absorbing-free substochastic walk on {L,V,B,R} (primary removed as source).
Pmat = np.array(
    [
        # L      V      B      R
        [0.20, 0.40, 0.30, 0.10],  # from L
        [0.05, 0.70, 0.20, 0.05],  # from V  (sponge)
        [0.25, 0.15, 0.45, 0.15],  # from B
        [0.05, 0.10, 0.10, 0.75],  # from R  (sponge-ish)
    ]
)
pin = Pmat.sum(axis=0)
pout = Pmat.sum(axis=1)
amp = pout / np.clip(pin, 1e-12, None)
roles = []
labels = ("L", "V", "B", "R")
for i, name in enumerate(labels):
    roles.append(
        {
            "site": name,
            "Pin": float(pin[i]),
            "Pout": float(pout[i]),
            "Pout_over_Pin": float(amp[i]),
            "role": "spreader" if amp[i] > 1.0 else "sponge",
        }
    )

exp6 = {
    "roles": roles,
    "note": "Roles are functions of a transition matrix. A scalar T(t) has no Pin or Pout.",
}


# ---------------------------------------------------------------------------
# Experiment 7 — lumped Gompertz/logistic Class A fit to a graph lump
# Fit a 2-parameter logistic to y_ff; residual vs site error of skip twin
# ---------------------------------------------------------------------------
def logistic_curve(t, r, K, t0=1.0):
    return K / (1.0 + (K / t0 - 1.0) * np.exp(-r * t))


def fit_logistic(y):
    def res(p):
        r, K = p
        return logistic_curve(T_OBS, r, K, t0=max(y[0], 1e-3)) - y

    out = least_squares(res, x0=np.array([0.12, 80.0]), bounds=([1e-4, 1.0], [2.0, 500.0]))
    return out.x, float(np.sqrt(np.mean(out.fun ** 2)))


p_log, logistic_rmse = fit_logistic(y_ff)
exp7 = {
    "logistic_r": float(p_log[0]),
    "logistic_K": float(p_log[1]),
    "lump_rmse_logistic_vs_filter_graph": logistic_rmse,
    "lump_rmse_skip_twin_vs_filter_graph": exp2["lump_rmse"],
    "comment": (
        "A two-parameter logistic can describe the lumped graph output to a "
        "comparable (or better) RMSE than a second graph twin, while remaining "
        "silent on first-site identity."
    ),
}


payload = {
    "disclaimer": (
        "Computational research only. Toy five-node anatomy. Not a medical "
        "device, not a patient cohort, not a metastasis-treatment claim. "
        "No document DOI."
    ),
    "nodes": list(NODES),
    "t_end": T_END,
    "n_obs": N_OBS,
    "seed": 5,
    "experiment_1_linear_homogeneous": exp1,
    "experiment_2_logistic_twins": exp2,
    "experiment_3_fisher": exp3,
    "experiment_4_route_profile": exp4,
    "experiment_5_occupancy_ctmc": exp5,
    "experiment_6_spreader_sponge": exp6,
    "experiment_7_class_a_fit": exp7,
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def fmt_eigs(d):
    e = d["eigs"]
    return ", ".join(f"{v:.3e}" for v in e)


lines = []
lines.append("# Identifiability experiment tables (in-silico)")
lines.append("")
lines.append("Research only. Toy five-node graph. Seed = 5.")
lines.append("")
lines.append("## Experiment 1 — linear homogeneous growth")
lines.append("")
lines.append("| Contrast | Value |")
lines.append("| --- | --- |")
lines.append(f"| Lumped RMSE (filter vs skip) | {exp1['lump_rmse_filter_vs_skip']:.3e} |")
lines.append(f"| Lumped max |·| (filter vs skip) | {exp1['lump_maxabs_filter_vs_skip']:.3e} |")
lines.append(f"| Lumped RMSE vs y=y0 e^{{rt}} | {exp1['lump_rmse_filter_vs_closed_form']:.3e} |")
lines.append(f"| Site-wise RMSE | {exp1['site_rmse_filter_vs_skip']:.4f} |")
lines.append(f"| First site (filter) | {exp1['first_site_filter'][0]} at t={exp1['first_site_filter'][1]} |")
lines.append(f"| First site (skip) | {exp1['first_site_skip'][0]} at t={exp1['first_site_skip'][1]} |")
lines.append("")
lines.append("Final occupancy (filter): " + ", ".join(f"{k}={v:.3f}" for k, v in exp1["final_occupancy_filter"].items()))
lines.append("")
lines.append("Final occupancy (skip): " + ", ".join(f"{k}={v:.3f}" for k, v in exp1["final_occupancy_skip"].items()))
lines.append("")
lines.append("## Experiment 2 — logistic soil twins")
lines.append("")
lines.append("| Contrast | Value |")
lines.append("| --- | --- |")
lines.append(f"| Lumped RMSE | {exp2['lump_rmse']:.4f} |")
lines.append(f"| Relative lumped RMSE | {exp2['rel_lump_rmse']:.4e} |")
lines.append(f"| Site-wise RMSE | {exp2['site_rmse']:.4f} |")
lines.append(f"| Primary-only RMSE | {exp2['primary_rmse']:.4f} |")
lines.append(f"| First site (filter) | {site_ff} at t={t_ff} |")
lines.append(f"| First site (skip) | {site_sk} at t={t_sk} |")
lines.append("")
lines.append("## Experiment 3 — FIM ranks on six edge rates")
lines.append("")
lines.append("| Observation map | n_obs | numerical rank / 6 | max eig | min pos eig | log10 κ |")
lines.append("| --- | --- | --- | --- | --- | --- |")
for name, d in (
    ("lumped sum", fim_lump),
    ("primary only", fim_primary),
    ("lesion-count analogue", fim_count),
    ("full site-wise state", fim_full),
):
    kap = d["log10_condition_pos"]
    kap_s = "—" if kap is None else f"{kap:.2f}"
    lines.append(
        f"| {name} | {d['n_obs']} | {d['rank']} / {d['n_params']} | {d['max_eig']:.3e} | {d['min_pos_eig']:.3e} | {kap_s} |"
    )
lines.append("")
lines.append("## Experiment 5 — occupancy waiting times")
lines.append("")
lines.append(f"KS statistic on waiting times: {exp5['ks_waiting_times']:.4f}")
lines.append(f"Mean wait filter/skip: {exp5['mean_wait_filter']:.3f} / {exp5['mean_wait_skip']:.3f}")
lines.append(f"Site hist filter: {exp5['site_hist_filter']}")
lines.append(f"Site hist skip: {exp5['site_hist_skip']}")
lines.append("")
lines.append("## Experiment 6 — spreader / sponge on a toy P")
lines.append("")
lines.append("| Site | Pin | Pout | Pout/Pin | role |")
lines.append("| --- | --- | --- | --- | --- |")
for row in roles:
    lines.append(
        f"| {row['site']} | {row['Pin']:.2f} | {row['Pout']:.2f} | {row['Pout_over_Pin']:.3f} | {row['role']} |"
    )
lines.append("")
lines.append("## Experiment 7 — Class A logistic fit to the graph lump")
lines.append("")
lines.append(f"r̂ = {p_log[0]:.4f}, K̂ = {p_log[1]:.2f}, lumped RMSE = {logistic_rmse:.4f}")
lines.append("")

OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(OUT_MD.read_text())
print(f"wrote {OUT_JSON} and {OUT_MD}")
