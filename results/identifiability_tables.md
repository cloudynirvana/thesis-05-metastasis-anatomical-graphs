# Identifiability experiment tables (in-silico)

Research only. Toy five-node graph. Seed = 5.

## Experiment 1 — linear homogeneous growth

| Contrast | Value |
| --- | --- |
| Lumped RMSE (filter vs skip) | 1.289e-08 |
| Lumped max |·| (filter vs skip) | 4.224e-08 |
| Lumped RMSE vs y=y0 e^{rt} | 3.937e-08 |
| Site-wise RMSE | 1.6771 |
| First site (filter) | L at t=0.5 |
| First site (skip) | V at t=1.0 |

Final occupancy (filter): P=2.111, L=3.308, V=8.332, B=8.220, R=2.561

Final occupancy (skip): P=0.687, L=10.497, V=3.199, B=3.193, R=6.957

## Experiment 2 — logistic soil twins

| Contrast | Value |
| --- | --- |
| Lumped RMSE | 0.0002 |
| Relative lumped RMSE | 6.2911e-06 |
| Site-wise RMSE | 10.6563 |
| Primary-only RMSE | 9.2457 |
| First site (filter) | L at t=1.5 |
| First site (skip) | V at t=0.5 |

## Experiment 3 — FIM ranks on six edge rates

| Observation map | n_obs | numerical rank / 6 | max eig | min pos eig | log10 κ |
| --- | --- | --- | --- | --- | --- |
| lumped sum | 81 | 5 / 6 | 8.348e+07 | 4.301e-02 | 9.29 |
| primary only | 81 | 4 / 6 | 1.558e+07 | 3.374e-11 | 17.66 |
| lesion-count analogue | 81 | 1 / 6 | 1.000e+10 | 1.000e+10 | 0.00 |
| full site-wise state | 405 | 6 / 6 | 1.243e+08 | 1.621e+04 | 3.88 |

## Experiment 5 — occupancy waiting times

KS statistic on waiting times: 0.0277
Mean wait filter/skip: 9.671 / 9.862
Site hist filter: {'L': 3175, 'V': 210, 'B': 395, 'R': 220}
Site hist skip: {'L': 827, 'V': 2343, 'B': 624, 'R': 206}

## Experiment 6 — spreader / sponge on a toy P

| Site | Pin | Pout | Pout/Pin | role |
| --- | --- | --- | --- | --- |
| L | 0.55 | 1.00 | 1.818 | spreader |
| V | 1.35 | 1.00 | 0.741 | sponge |
| B | 1.05 | 1.00 | 0.952 | sponge |
| R | 1.05 | 1.00 | 0.952 | sponge |

## Experiment 7 — Class A logistic fit to the graph lump

r̂ = 0.1575, K̂ = 141.49, lumped RMSE = 1.0255

