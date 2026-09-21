# Metastasis as Stochastic Spreading on Organ-to-Organ Anatomical Graphs: Adequacy of Local Tumour-Burden ODEs under Lumped Outputs

**Thesis #5 — computational research thesis**
**Author:** Kelechi Emeka Ogbonna
**Correspondence:** kelechiogbonna300@gmail.com · https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs
**Date:** 21 September 2026
**Format:** B.Sc. project chapter structure (Nile University style) for journal / thesis handoff
**Status:** Computational identifiability study on a toy anatomical graph. Not a clinical result. Not a metastasis-treatment claim.
**Citation style:** numbered Vancouver [n]. DOI fields appear only for Crossref- or PubMed-verified journal records.
**DOI:** none registered for this document. Do not invent one.

This manuscript is hub topic NP-05 [53]. It is not a restatement of theses 01–04 [49–52]. It is not the 2022 Nile University B.Sc. *Carica papaya* AgNP antidiabetic project. Results in Chapter Four are in-silico numbers from `scripts/identifiability_experiment.py`. They are not patient outcomes.

---

## Title page

**METASTASIS AS STOCHASTIC SPREADING ON ORGAN-TO-ORGAN ANATOMICAL GRAPHS: ADEQUACY OF LOCAL TUMOUR-BURDEN ODES UNDER LUMPED OUTPUTS**

BY

**KELECHI EMEKA OGBONNA**

A COMPUTATIONAL RESEARCH THESIS
(IN-SILICO IDENTIFIABILITY STUDY)

SUBMITTED AS A CITEABLE MANUSCRIPT FOR JOURNAL / THESIS HANDOFF

PROJECT CONFLUENCE
INDEPENDENT COMPUTATIONAL RESEARCH

SUPERVISOR: not appointed for this computational deposit

SEPTEMBER 2026

---

## Declaration

I, Kelechi Emeka Ogbonna, hereby declare that this computational research thesis titled "Metastasis as Stochastic Spreading on Organ-to-Organ Anatomical Graphs: Adequacy of Local Tumour-Burden ODEs under Lumped Outputs" was carried out by me. The findings reported here are in-silico. They are not wet-lab measurements, not patient outcomes, and not a claim of cure, dose, or clinical decision support. No identifier (DOI, ORCID, journal acceptance) has been invented.

_________________________ _______________________
Kelechi Emeka Ogbonna Date

---

## Abstract

Local tumour-burden ordinary differential equations (ODEs) treat disease as a scalar, or a small vector, attached to one site. Metastasis, as written in the anatomical-network literature, is a stochastic process on a directed graph whose nodes are organs or nodal stations and whose edges are haematogenous or lymphatic routes [24,26–32]. This thesis asks whether the local ODE remains an adequate in-silico object once that graph is admitted, or whether graph observables remain unidentified under the lumped outputs that current burden models actually see.

The methods contrast two model classes and then measure the contrast on a toy five-node anatomy (primary, lung, liver, bone, brain). Class A is a local growth law — Gompertz, logistic, or a lumped multi-compartment cancer-state ODE — observed through primary volume, a summed metastatic burden, a lesion-count analogue, or a first-event time [14–16,18–22,42]. Class B is spreading on an organ-to-organ graph: a conservative transfer ODE, a logistic-soil ODE, or a binary occupancy chain [24,26–32]. Identifiability is used as a refusal rule and as a finite-difference Fisher information rank [36–42].

Under lumped outputs the following stay unidentified: the occupancy vector, first-site identity, the transition matrix, spreader versus sponge roles, transit times, organ-specific colonization, the split between primary shedding and secondary seeding, and self-seeding flux [26–32,33–35,42]. Newton and colleagues had to assume a steady-state match to autopsy frequencies because the walk was underdetermined [26,27,32]. Álvarez-Arenas and colleagues showed that even a two-parameter growth-and-dissemination model is not practically identifiable from a distant-metastasis-free survival (DMFS) curve unless the fraction with metastasis at diagnosis is supplied [42].

Chapter Four reports the in-silico laboratory. With homogeneous linear growth, two anatomies that transfer mass on different edges produce lumped trajectories identical to \(1.3 \times 10^{-8}\) RMSE while site-wise RMSE is 1.68 and first sites differ (lung versus liver). With logistic soil, a skip-path twin can be fitted to a filter-flow lump at RMSE \(2.3 \times 10^{-4}\) (relative \(6.3 \times 10^{-6}\)) while site-wise RMSE remains 10.66 and the first detectable site again flips. Finite-difference Fisher information on six edge rates is rank 5/6 and ill-conditioned (\(\log_{10}\kappa \approx 9.3\)) from the lumped sum, rank 4/6 from primary volume, rank 1/6 from a lesion-count analogue, and rank 6/6 from the full site-wise state. An occupancy chain with matched mean waiting time (Kolmogorov–Smirnov statistic 0.028) still sends first hits to lung in 3175/4000 filter-flow paths and to liver in 2343/4000 skip paths. A two-parameter logistic can describe the same lumped curve (RMSE 1.03) and remain silent on every graph coordinate.

GLOBOCAN 2024 estimates, published 2026, place the contemporary burden at about 20.6 million diagnoses and 9.8 million deaths [1]. That statistic motivates computational work on dissemination. It is not a graph parameter and not a product claim [2,54]. This document does not claim a treatment of metastasis, a targeting list for “spreader” organs, or an identified \(\Theta\). Scientific success here is a typed distinction between lumped burden and graph observables, with unidentified symbols left labelled as such [36–41].

**This thesis is research only. It is not a medical device, not clinical decision support, and not a wet-lab study.**

---

## Keywords

computational oncology; metastasis; anatomical graphs; Markov chains; identifiability; lumped outputs; tumour-burden ODE; seed and soil; filter-flow; Fisher information; research-only; not a medical device

---

## Table of Contents

DECLARATION
ABSTRACT
Table of Contents
List of tables and figures

CHAPTER ONE — INTRODUCTION
 1.1 Background to the study
 1.2 STATEMENT OF RESEARCH PROBLEM
 1.3 JUSTIFICATION OF STUDY
 1.4 AIM AND OBJECTIVES OF THE STUDY
 1.5 SIGNIFICANCE OF THE STUDY
 1.6 SCOPE OF THE STUDY

CHAPTER TWO — LITERATURE REVIEW
 2.1 Seed, soil, filter, and cascade
 2.2 Local growth laws and spatially unresolved metastasis
 2.3 Metastasis networks and Markov diagrams
 2.4 Self-seeding as a graph walk
 2.5 Identifiability of dynamical biological models
 2.6 What theses 01–04 already claimed

CHAPTER THREE — MATERIALS AND METHODS
 3.1 Study design and honesty statement
 3.2 Honesty gates
 3.3 Class A and Class B objects
 3.4 Observation maps
 3.5 Computational laboratory
 3.6 What was not done

CHAPTER FOUR — RESULTS
 4.1 Linear homogeneous growth: the graph vanishes from the lump
 4.2 Logistic-soil twins: matched lump, different anatomy
 4.3 Fisher information ranks under four maps
 4.4 Occupancy waiting times versus first-site identity
 4.5 Spreader and sponge roles are undefined on \(T(t)\)
 4.6 A Class A logistic can describe a graph lump
 4.7 Synthesis: what stays unidentified

CHAPTER FIVE — DISCUSSION, CONCLUSION AND RECOMMENDATION
 5.1 Discussion
 5.2 Conclusion
 5.3 Recommendation

REFERENCES
DISCLAIMER

---

## List of tables and figures

**Table 3-1.** Honesty gates used as sequential, falsifiable methods controls.
**Table 3-2.** Lumped observation maps and the coordinates they erase.
**Table 4-1.** Experiment 1: linear homogeneous growth, filter-flow versus skip-path.
**Table 4-2.** Experiment 2: logistic-soil twins fitted on the lumped sum.
**Table 4-3.** Finite-difference Fisher information ranks on six edge rates.
**Table 4-4.** Occupancy-chain first-event times versus first-site counts (4000 paths).
**Table 4-5.** Spreader / sponge roles on a toy transition matrix.
**Table 4-6.** Graph observables that remain unidentified under lumped outputs.

Results in Chapter Four are computational experiments on a toy five-node graph. They are not fabricated patient outcomes.

---

# CHAPTER ONE

## 1.0 INTRODUCTION

### 1.1 Background to the study

A local tumour-burden ODE answers how much tissue is present, at one site or as a sum, as a function of time [14–17]. Metastasis answers a different question: which organs are occupied, in what order, along which routes, and with what waiting times [5–10,24,26–32]. Collapsing the second question into the first treats a scalar as a sufficient statistic for a directed anatomical network.

Paget’s 1889 seed-and-soil remark, Ewing’s later mechanical alternative, and the modern cascade reviews agree on one empirical fact even when they disagree on mechanism: secondary growth is organ-patterned, inefficient, and often occult at the scale of a clinical scan [3–10,12,13]. Circulating cells are numerous; colonies are rare [5,6]. Parallel progression and dormancy further imply that a late, lumped burden can hide an earlier occupancy pattern [12,13]. None of those reviews identifies a coefficient in a local ODE.

Two modelling traditions now sit side by side. One continues the classical growth-law programme: Laird’s Gompertz observation, Gerlee’s warning that growth laws are under-determined by bulk curves, Benzekry and colleagues’ comparison of ODE families on experimental volume series, and the Iwata transport equation for a size distribution of metastases that is still spatially unresolved [14–18]. The other treats organs as nodes and dissemination as a walk or an occupancy process on a graph built from claims data, autopsy series, or anatomical flow [24–32]. Chen and colleagues introduced metastasis networks from Medicare co-occurrence [24]. Newton and colleagues fitted Markov chains to untreated autopsy frequencies and, later, to a longitudinal breast-cancer series [25–28]. Scott, Kuhn, Anderson, Gerlee and colleagues wrote haematogenous spread as filter-flow through successive capillary beds and showed that self-seeding of the primary, as a growth driver, requires secondary deposits [29–31]. Gerlee and Johansson then replaced Newton’s steady-state assumption with a temporal, anatomically constrained occupancy model [32].

The failure mode this thesis names is not that either tradition is empty. It is that a laboratory can keep a local ODE, observe only a lumped output, and still speak as if seeded sites, routes, and organ-specific colonization had been identified. Structural identifiability asks whether a unique parameter vector is consistent with noise-free input–output data [36–40]. Practical identifiability asks whether finite, noisy data actually constrain those parameters [37,41,42]. A lumped map \(y(t)=\sum_i x_i(t)\), or a primary-only volume, or a DMFS curve, is a many-to-one observation of a graph process. Many-to-one maps hide coordinates. The coordinates that stay hidden are the subject of this manuscript.

GLOBOCAN 2024 estimates (about 20.6 million diagnoses and 9.8 million deaths across 34 cancers and 186 countries) are setting context [1,2]. They are not CONFLUENCE parameters, not edge weights, and not a licence to treat [54]. WHO language that many cancers can be cured if found early and treated well is a health-system statement about staged, treatable disease [2]. It is not a claim that an anatomical-graph model treats metastasis.

Project Confluence already freezes a 15-dimensional local cancer-state ODE behind knowledge gates [48,49]. Complexity Science cards pathology without writing guidelines into coefficients [50]. Disease Profiles export research objects that are not charts [51]. Thesis 04 writes occult residual disease as a hybrid mode rather than a smuggled continuous state [52]. Those documents do not ask whether a lumped burden identifies an organ-to-organ graph. This one does.

### 1.2 STATEMENT OF RESEARCH PROBLEM

Does a local tumour-burden ordinary differential equation remain an adequate in-silico object once dissemination is posed as a stochastic process on an organ-to-organ anatomical graph, or do graph observables remain unidentified under current lumped outputs [15–18,24,26–32,36–42]?

That is the research problem. It is a computational and medical-methods problem. It is not a claim to treat, dose, resect, irradiate, or otherwise manage metastatic disease [2,31,54].

A local burden model — Gompertz, logistic, Bertalanffy, a Gomp-Exp splice, the Iwata colony-size transport equation closed by a shedding boundary, or a lumped multi-compartment cancer-state ODE — is built to track how much tumour is present [14–22]. Its natural outputs are volumes, summed burdens, and, at one further remove, time-to-event curves derived from a detection threshold [20–22,42]. An anatomical-graph model is built to track where tumour is present. Its state is an occupancy vector or a site-wise burden on a directed network whose edges are vessels, lymphatics, or empirically scored co-occurrence links [24,26–32]. Self-seeding, primary reseeding, and metastasis-to-metastasis reseeding are distinct walks on that network, not synonyms for a larger scalar [27,30,33–35].

The two objects coincide only for questions that are invariant under every graph trajectory sharing the same lumped output. Questions about first-site identity, subsequent path, spreader versus sponge roles, organ-specific colonization, and the split between direct and secondary seeding are not invariant [26–28,32]. Newton’s autopsy chain was underdetermined until a steady-state assumption was imposed [26,27,32]. A DMFS curve does not identify growth and dissemination as a pair unless further summary statistics are supplied [42]. Total metastatic burden can be described while the size distribution of colonies remains unidentified [21]. Those are identifiability facts already in the literature. The problem is to keep them attached to the lumped observation map, so that a local ODE is not silently promoted to a dissemination model, and to measure the many-to-one map on a toy graph that can be integrated, fitted, and ranked without pretending to be a cohort.

Success is a typed distinction, a labelled list of unidentified graph observables, and computational ranks that fail closed. Success is not a survival difference, not a targeting order of organs, and not an identified \(\Theta\) [36–41,54].

### 1.3 JUSTIFICATION OF STUDY

Existing modelling habits fail in documented ways that this study is built to catch.

**Overclaiming.** GLOBOCAN burden figures and WHO early-detection language are health-system context [1,2]. They are not edge weights. Mathematical oncology supplies in-silico laboratories for growth, resistance, and control [17]; adaptive-therapy papers treat dosing as a selection process in a local competitive ecology [45]. Neither literature identifies an organ-to-organ transition matrix, and neither is cited here as a metastasis-treatment protocol [45,54]. Scott and colleagues titled a filter-flow paper as a “non-genetic paradigm for personalised cancer therapy” [31]. This thesis takes the anatomical constraint from that paper — successive capillary beds as filters — and refuses the therapy claim. Newton and colleagues noted that spreader/sponge classification might later inform oligometastatic targeting [28]. That sentence is a motivation in their discussion. It is not a result of this manuscript and not a care recommendation [54].

**Lumped-output smuggling.** A primary volume series identifies, at best, a growth-law family, and even that family is not unique: Gerlee called the situation a model muddle [15]; Benzekry and colleagues showed that several classical ODEs can describe the same experimental curves [16]. Iwata, Kawasaki and Shigesada replaced a single volume with a size distribution of metastatic colonies still living in an unresolved spatial domain [18]. Subsequent analysis and mixed-effects fits can recover shedding and growth from total burden in mice and still fail the size distribution unless foci interact [19–21]. Álvarez-Arenas and colleagues reduced metastasis to two scalars, a growth rate \(\alpha\) and a dissemination rate \(\mu\), and showed that a DMFS curve does not practically identify the pair without the fraction of patients already metastatic at diagnosis [42]. If two scalars are already weakly seen from a survival curve, a transition matrix on tens of organs is not seen from a single summed burden.

**Missing graph coordinates.** Chen and colleagues showed that metastasis has a network topography in claims data [24]. DiSibio and French tabulated organ-resolved autopsy frequencies in untreated decedents [25]. Newton and colleagues turned those frequencies into a Markov chain and classified sites as spreaders or sponges [26,27]; a later breast-cancer chain made the first metastatic site as informative, in their cohort, as receptor subtype for subsequent path [28]. Gerlee and Johansson stated the underdetermination explicitly: without anatomical sparsity and a time proxy, site-to-site rates are not recoverable from incidence tables [32]. Phylogenetic studies of lethal metastatic prostate cancer show branching, reseeding, and organ-restricted clades that a scalar burden cannot encode [43,44]. Those coordinates are the gap. Theses 01–04 close other gaps — knowledge-graph provenance, guideline-as-constraint, research-object export, and hybrid occult modes — and do not ask this anatomical-network question [49–53].

**What this study therefore does.** It writes the two model classes against one observation map, lists the graph observables that lumped outputs do not identify, and measures the map on a toy five-node graph whose code and numbers sit in this repository [36–42,54]. It does not fit a new autopsy series or a new Markov chain to human data.

### 1.4 AIM AND OBJECTIVES OF THE STUDY

The aims are computational. Success is a usable identifiability argument plus reproducible numbers, not a waiting-time estimate in a person.

1. State the adequacy criterion for a local tumour-burden ODE once dissemination is a graph process: invariance of the research question under lumped-equivalent trajectories [15,16,36–41].
2. Write Class A (local / spatially unresolved burden dynamics) and Class B (stochastic spreading on an organ-to-organ anatomical graph) as distinct formal objects [14–22,24,26–32].
3. Name the lumped observation maps actually used — primary volume, summed metastatic burden, detection-threshold event times, lesion counts, DMFS curves — and show they are many-to-one [16,20–22,42].
4. Measure those maps on a toy five-node graph: construct lumped-equivalent twins, rank a finite-difference Fisher information matrix, and compare occupancy waiting times with first-site identity.
5. List graph observables that remain unidentified under those maps, citing the underdetermination, filter-flow, size-distribution, and DMFS identifiability results already published [21,26,27,31,32,42].
6. Refuse clinical metastasis-treatment claims, including spreader-targeted therapy, oligometastatic ablation as a consequence of a Markov diagram, and filter-flow “personalised therapy” [28,31,54].

**Non-aims.** Estimating a treatment effect. Identifying a human transition matrix. Promoting CONFLUENCE, OnCo, NSTG, or a Disease Profile board into an anatomical graph [49–51]. Editing `CancerODE`. Recommending resection or irradiation of a “spreader” organ.

### 1.5 SIGNIFICANCE OF THE STUDY

**Scientific significance for researchers.** The work treats metastasis as a graph process whose state is occupancy and route, not only mass [5–10,24,26–32]. Laboratories that already run a local cancer-state ODE — including the frozen 15-dimensional CONFLUENCE lineage cited only as an example of a lumped object [48,49] — gain an explicit test: if the research question changes when two graph trajectories share the same summed burden, the local ODE is not an adequate object for that question. Unidentified symbols stay labelled [36–41]. Chapter Four supplies a numerical form of that test that can be re-run from `scripts/identifiability_experiment.py`.

**Methodological significance.** Identifiability literature becomes a refusal rule for anatomical networks, as it already is for knowledge-to-parameter promotion in thesis 01 [36–41,49]. The contribution is the observation map and a toy rank table, not a new structural-identifiability algorithm and not a re-fit of Newton’s transition matrix. Efficiency, if claimed at all, is research-operational: a laboratory can ask whether it needs site-resolved occupancy, waiting times, or phylogenetic paths *before* writing another right-hand side.

**What this significance is not.** It is not clinical decision support, not a medical device, not a dose, not a cure, and not a metastasis-treatment claim [2,54]. It is not a recommendation to irradiate or resect spreader organs. It is not personalized prediction of the next metastatic site as a care product, even though Chen, Newton, and Gerlee discuss prediction inside research cohorts [24,28,32]. GLOBOCAN figures do not become colonization rates [1]. Translation after biological and clinical validation remains unclaimed. The significance of the study is methodological honesty for researchers, not a path to a clinic.

### 1.6 SCOPE OF THE STUDY

**In scope.** Bibliographic contrast of Class A and Class B; a toy five-node ODE / occupancy laboratory; finite-difference Fisher ranks; a labelled unidentified list; research-only refusal rules.

**Out of scope.** Patient-identifiable data. New autopsy or SEER fits. New Markov-chain estimates on human tables. Controller priors. Doses. Imaging-interval recommendations. Any claim that a person is metastatic, oligometastatic, or disease-free.

**Spatial scale.** Organ-to-organ anatomy. Not a PDE of a desmoplastic primary (hub NP-02). Not hybrid occult modes (thesis 04 / NP-03) except as a neighbouring refusal [52,53].

**Time bound.** Computational deposit dated 21 September 2026. No document DOI.

---

# CHAPTER TWO

## 2.0 LITERATURE REVIEW

### 2.1 Seed, soil, filter, and cascade

Paget wrote that secondary growths are not randomly scattered [3]. Fidler restated seed-and-soil as a pathogenesis, not a slogan [4]. Chambers, Groom and MacDonald separated dissemination from colonization and documented metastatic inefficiency [5]. Gupta and Massagué, Nguyen, Bos and Massagué, Valastyan and Weinberg, Obenauf and Massagué, and Lambert, Pattabiraman and Weinberg organised the cascade from local invasion through circulation to organ-specific colonization [6–10]. Hanahan and Weinberg list activating invasion and metastasis among the hallmarks; a hallmark is not a rate constant [11]. Klein’s parallel-progression account and Aguirre-Ghiso’s dormancy review imply that occupancy can exist below a detection floor for long times [12,13]. Those statements are knowledge. They are not \(\Theta\).

Scott, Kuhn and Anderson proposed unifying haematogenous metastasis as successive filtration through capillary beds rather than as a single genetic switch [29]. Scott, Fletcher, Maini, Anderson and Gerlee then wrote an explicit filter-flow anatomy: venous-side cells meet lung as first filter; further arterial spread is conditional on that filter, on self-seeding, and on secondary seeding [31]. The anatomy is the usable object here. The “personalised cancer therapy” clause in their title is not adopted [31,54].

### 2.2 Local growth laws and spatially unresolved metastasis

Laird described experimental tumour growth as Gompertzian [14]. Gerlee reviewed the subsequent zoo of growth laws and the inability of bulk curves to pick a unique form [15]. Benzekry and colleagues compared classical ODEs on experimental volume series [16]. Altrock, Liu and Michor surveyed quantitative cancer models more broadly, including stochastic and spatial families, without collapsing them into one scalar [17].

Iwata, Kawasaki and Shigesada wrote a transport equation for the size distribution of metastatic colonies, with a boundary condition for shedding from the primary [18]. Barbolosi and colleagues analysed that equation [19]. Hartung and colleagues fitted related mixed-effects models to bioluminescence in mice and reported peritoneal metastatic growth that ODE models could not describe [20]. Baratchart and colleagues fitted primary-plus-total-burden data in a renal-cell xenograft and then failed the MRI size distribution until neighbouring foci were allowed to merge [21]. Benzekry and colleagues coupled pre-surgical primary volume to post-surgical metastatic burden, still without an organ graph [22]. Franssen, Lorenzi, Burgess and Chaplain placed invasion and distant growth on a spatially explicit hybrid grid — a different spatial scale from organ-to-organ anatomy, and still not a lumped ODE [23]. The pattern is consistent: moving off a single volume exposes coordinates that the volume did not identify.

### 2.3 Metastasis networks and Markov diagrams

Chen, Blumm, Christakis, Barabási and Deisboeck defined a cancer metastasis network on Medicare claims: nodes are primary and metastatic sites, links are co-occurrence strengths, and the network supports anterograde and retrograde prediction *inside that claims experiment* [24]. DiSibio and French reported metastatic patterns from a large autopsy series of untreated cancers, the empirical table later used by Newton [25]. Newton, Mason, Bethel, Bazhenova, Nieva, Kuhn and colleagues constructed a discrete Markov chain on that table for primary lung cancer, treating circulating cells as random walkers [26]. A follow-up Monte Carlo study classified sites as spreaders or sponges and distinguished self-seeding of the primary, reseeding of the primary from a metastasis, and reseeding among metastases [27]. In a 446-patient breast-cancer series, Newton, Mason, Venkatappa, Jochelson, Hurt, Nieva, Comen, Norton and Kuhn estimated subtype-specific transition probabilities and reported that the first metastatic site structured subsequent paths and survival in that cohort [28]. Those are research-cohort descriptions. They are not protocols.

Gerlee and Johansson replaced the steady-state assumption. They modelled nodes as binary (negative/positive), restricted flow to anatomically neighbouring stations, split primary shedding \(\lambda\) from metastatic shedding \(\varphi\), and used primary stage as a time proxy to infer *relative* rates on tongue-cancer lymphatic stations and on SEER ovarian patterns [32]. They state that Newton’s transition matrix was underdetermined from incidence alone [32]. That sentence is the justification for keeping graph parameters out of a lumped ODE.

### 2.4 Self-seeding as a graph walk

Norton and Massagué asked whether cancer is a disease of self-seeding [33]. Kim and colleagues supplied mouse evidence that circulating cells can re-infiltrate a primary [34]. Comen, Norton and Massagué discussed clinical implications [35]. Scott, Basanta, Anderson and Gerlee showed, in a mathematical treatment, that self-seeding as a *driver of primary growth* requires secondary metastatic deposits; otherwise the return flux is negligible [30]. A primary-volume ODE that absorbs an extra growth term labelled “self-seeding” without a secondary-site state has smuggled a graph walk into a local parameter.

### 2.5 Identifiability of dynamical biological models

Bellman and Åström defined structural identifiability [36]. Raue and colleagues distinguished structural from practical identifiability via profile likelihood [37]. Chis, Banga and Balsa-Canto compared computational tests for systems-biology models [38]. Villaverde, Barreiro and Papachristodoulou, and Villaverde’s later observability paper, treat unobservability and unidentifiability as properties of the model-plus-output pair [39,40]. Wieland and colleagues restated the distinction for current practice [41]. Álvarez-Arenas and colleagues applied practical identifiability to a mechanistic DMFS model: two parameters, growth and dissemination, are not a free lunch from a survival curve [42]. Naxerova and Jain, and Gundem and colleagues, show that reconstructing metastatic paths needs phylogeny, not a summed burden [43,44]. This thesis uses that literature as a refusal rule and as the warrant for a finite-difference Fisher rank on a toy graph. It does not report a new symbolic identifiability certificate for Newton’s 50-site chain.

### 2.6 What theses 01–04 already claimed

**Thesis #1 — OnCo adapter.** How to bind an oncology knowledge graph to a frozen dynamical cancer-state model without skip-level promotion into \(\Theta\) [49]. Architectural evidence: read-only adapter, refusal tests, LDHA is not `p_lactate`. Anatomical graphs are not its object.

**Thesis #2 — NSTG CaseCards.** How to explore complex in-silico pathology under NSTG as a qualitative knowledge constraint, never auto-translated into ODE coefficients [50]. The explorer never opens an evidence gate. The card is not an organ graph.

**Thesis #3 — Disease Profile schema.** How to export a versioned research object for systemic personalized-medicine *research*, not CDS [51]. The board is not a Markov chain.

**Thesis #4 — occult as hybrid switching.** Quiescence, angiogenic pause, and immune-held latency as named modes, so occult never becomes a smuggled continuous state [52]. Occult occupancy on a graph is a neighbouring missing-output problem; it is not re-derived here as a Filippov system.

Hub `NEXT_PAPERS.md` item NP-05 is the charter for this manuscript [53]. NP-02 (spatial transport) and NP-03 (hybrid occult) are neighbouring problems. They are not this problem.

---

# CHAPTER THREE

## 3.0 MATERIALS AND METHODS

### 3.1 Study design and honesty statement

**Design.** Computational research. Two layers: (i) a bibliographic and formal contrast of Class A and Class B against named observation maps; (ii) a reproducible in-silico laboratory on a toy five-node anatomy, reported in Chapter Four.

**Materials.**

- Published anatomical-network and Markov metastasis models [24,26–28,32].
- Filter-flow and self-seeding mathematics [29–31,33–35].
- Classical and metastatic growth-law papers, including size-distribution and mixed-effects fits [14–22].
- Identifiability and observability papers [36–42].
- Cascade and organotropism reviews used only as knowledge [3–13].
- Frozen CONFLUENCE lineage `confluence_v2_15d` named only as an example of a lumped local cancer-state ODE; it is not refit and its right-hand side is not edited [48,49].
- Theses 01–04 and the hub catalogue, cited so this problem is not collapsed into theirs [49–53].
- Python 3, NumPy, SciPy (`solve_ivp`, `least_squares`); script `scripts/identifiability_experiment.py`; seed 5; results in `results/identifiability_results.json`.

**Honesty.** Simulated trajectories are computational artefacts. They are not patient outcomes, not a protocol, and not a dose [54]. Spreader/sponge is a network role in a fitted diagram [27,28]. It is not an indication. Filter-flow is an anatomical constraint [31]. It is not personalized therapy. The five nodes are a cartoon of venous-to-lung filter-flow, not a human atlas.

### 3.2 Honesty gates

The public protocol is sequential and falsifiable. It is not a treatment path.

**Table 3-1.** Honesty gates used as sequential, falsifiable methods controls.

| Gate | Requirement |
| --- | --- |
| 0 | Research-only scope. Not a medical device. Not clinical decision support. Not a metastasis-treatment claim. [54] |
| 1 | Provenance: which paper, which cohort class (autopsy, claims, xenograft, SEER, toy graph), which spatial scale. |
| 2 | Model class named: local burden ODE (A) or anatomical graph process (B). |
| 3 | Observation map named: primary volume, site-wise occupancy, summed burden, event time, lesion count, DMFS. |
| 4 | Parameter: model id, symbol, units, estimator, uncertainty, identifiability. Unidentified ≠ established. [36–42] |
| 5 | Prediction labelled as computational. |
| 6 | Held-out / external / baseline validation — not claimed for a human fit in this repository. |
| 7 | An experiment that could show the claim is wrong (site-resolved occupancy, waiting times, or phylogeny that splits lumped-equivalent trajectories). |
| 8 | Translation only after biological and clinical validation this repository does not claim. [2,54] |

Scientific success is: traceability → mathematical validity → identifiability → labelled unidentified remainder. Disease eradication is not a success criterion of this thesis [2,54].

### 3.3 Class A and Class B objects

**Class A — local tumour-burden dynamics.** Let \(T(t)\ge 0\) denote a local or spatially unresolved tumour burden (cells, volume, or a proxy). A typical closed ODE is

\[\dot T = g(T;\theta),\qquad y(t)=h(T(t)),\]

with \(g\) Gompertz, logistic, Bertalanffy, exponential, or a Gomp-Exp splice [14–16], and \(h\) the identity, a noisy volume, or a threshold that yields an event time. Multi-compartment local models enlarge \(T\) to a vector \(X(t)\in\mathbb{R}^d\) still attached to one site or to an unresolved sum [17,48]. They do not, by that enlargement alone, become organ graphs.

Iwata-type models replace \(T\) by a density \(u(x,t)\) of colonies of size \(x\) [18,19]. The spatial domain of \(x\) is size, not anatomy. CONFLUENCE `confluence_v2_15d` is cited only as a lumped cancer-state ODE already fenced by thesis 01’s knowledge gates [48,49]. This thesis does not open that right-hand side and does not add organ nodes to it.

**Class B — stochastic spreading on an anatomical graph.** Let \(G=(V,E)\) be a directed graph. Vertices \(V=\{1,\ldots,n\}\) are organs, nodal stations, or other anatomical compartments. Edges \(E\) are feasible routes: lymphatic drainage, venous-to-lung filter, arterial distribution, transcoelomic spread, or empirically scored links [24,29–32]. Three representations appear in the cited literature and are used here as a family.

1. **Markov walk.** A circulating walker has transition matrix \(P=(P_{ij})\). Site frequencies in the large-time limit are a left eigenvector if a steady state exists. Newton and colleagues estimated \(P\) from autopsy histograms under that assumption [26,27]. Occupancy of walkers at nodes yields spreader/sponge roles from in- and out-flow [27,28].
2. **Binary occupancy chain.** Each node \(i\) has state \(\sigma_i\in\{0,1\}\). A positive node sheds along outgoing edges at rates \(\lambda\) (if primary) or \(\varphi\) (if metastatic). Skip-edges are forbidden or rare. Gerlee and Johansson used this form so that the number of free parameters tracked anatomical links rather than a dense \(n\times n\) matrix [32].
3. **Filter-flow coupled ODE.** Site-wise burden \(x(t)\in\mathbb{R}^n_{\ge 0}\) with local growth plus linear transfer:

\[\dot x_i = r_i x_i (1 - x_i/K_i) + \sum_j W_{ij} x_j - \bigl(\sum_k W_{ki}\bigr) x_i.\]

\(W_{ij}\) is the seeding rate from source \(j\) into target \(i\). Haematogenous passage is a cascade of filters, not an all-to-all genetic lottery [29,31]. Self-seeding is an edge back to the primary, not a local growth coefficient [30,33–35].

Adequacy criterion (research-scoped). A Class A model with output \(\Phi\) is adequate for a question \(Q\) if and only if every pair of Class B trajectories with the same \(\Phi\)-path give the same answer to \(Q\). If \(Q\) asks for a seeded set, a first site, a route, a waiting time, a spreader/sponge role, or a secondary-seeding fraction, Class A is not adequate.

### 3.4 Observation maps

Write \(\Phi\) for the map from graph state to what a local ODE typically sees.

**Table 3-2.** Lumped observation maps and the coordinates they erase.

| Map | Formula (schematic) | What it erases |
| --- | --- | --- |
| Primary only | \(y=x_{\mathrm{primary}}\) or \(y=T\) | All downstream occupancy |
| Summed burden | \(y=\sum_{i\in V} x_i\) | Which nodes contribute |
| Detectable sum | \(y=\sum_i 1_{x_i\ge \tau} x_i\) | Occult occupancy below \(\tau\) [12,13] |
| Count of lesions | \(y=\#\{i:x_i\ge\tau\}\) | Identity of \(i\), routes, times |
| First-event time | \(y=\inf\{t:\max_{i\neq\mathrm{primary}}x_i\ge\tau\}\) | Which site fired, later path |
| DMFS curve | population survival of first-event times | Site, route, growth vs dissemination split [42] |
| Autopsy histogram | empirical \(\pi_i\) at death | Times, order, transients [25–27] |

### 3.5 Computational laboratory

The laboratory is a five-node cartoon: primary (P), lung (L), liver (V), bone (B), brain (R). Initial condition \(x(0)=(1,0,0,0,0)\). Integration horizon \(t\in[0,40]\) with 81 equally spaced observation times. Seed 5.

**Experiment 1 — linear homogeneous knockout.** Set every local growth rate to \(r=0.08\) and drop the logistic term. Transfer is conservative. Then \(\dot y = r y\) independently of \(W\), so \(y(t)=y_0 e^{rt}\). Two distinct \(W\) matrices (filter-flow: primary sheds to lung; skip-path: primary sheds to liver and bone) are integrated and compared on \(y\) and on \(x\).

**Experiment 2 — logistic-soil twins.** Filter-flow uses heterogeneous \(r\) and \(K\) (soil) and lung-first edges. A skip-path twin with six free edge rates plus \(r\) and \(K\) is fitted by nonlinear least squares to the filter-flow lumped sum. Site-wise error and first detectable site (\(\tau=0.05\)) are then compared.

**Experiment 3 — Fisher ranks.** Around the fitted skip-path, six edge rates are perturbed by a relative step \(10^{-5}\). A Gaussian Fisher information matrix \(F=S^\top S\) is assembled for four observation maps: lumped sum (81 samples), primary only (81), lesion-count analogue (81), and the full site-wise state (405). Numerical rank uses a relative singular-value cutoff of \(10^{-8}\). Conditioning is \(\log_{10}\) of the ratio of the largest to the smallest positive eigenvalue. This is a local, noise-free sensitivity rank, not a profile-likelihood certificate [37,41].

**Experiment 4 — route profile.** Total primary shedding is held at \(c=0.05\) while the lung share \(\alpha\) slides from 0 to 1. Lumped and site-wise sum-of-squares versus the \(\alpha=1\) reference are recorded. This shows that heterogeneous soil can make the lump *see* a mixture without identifying the route.

**Experiment 5 — occupancy chain.** Competing exponential clocks from an occupied primary to \(\{L,V,B,R\}\). Two rate vectors share the same total rate (hence the same waiting-time law in expectation) and differ in site identity. 4000 paths each; two-sample Kolmogorov–Smirnov statistic on waiting times; site histograms.

**Experiment 6 — spreader/sponge.** A toy four-site substochastic \(P\) yields \(P_{\mathrm{out}}/P_{\mathrm{in}}\) following Newton’s ratio [27,28]. The point is definitional: a scalar \(T(t)\) has no \(P_{\mathrm{in}}\).

**Experiment 7 — Class A fit.** A two-parameter logistic is fitted to the filter-flow lumped sum from Experiment 2. RMSE is compared with the skip-path twin.

Code: `scripts/identifiability_experiment.py`. Tables: `results/identifiability_tables.md`. Machine-readable dump: `results/identifiability_results.json`.

### 3.6 What was not done

No human table was re-fitted. No CONFLUENCE right-hand side was edited. No OnCo record, NSTG sentence, or Disease Profile board was written into \(W\), \(\lambda\), \(\varphi\), or a soil coefficient [49–51]. No dose was computed. No spreader organ was nominated for treatment [28,31,54]. Gate 8 remains unclaimed.

---

# CHAPTER FOUR

## 4.0 RESULTS

All numbers in this chapter come from one run of `scripts/identifiability_experiment.py` with seed 5 [46,47]. They describe a toy graph. They do not describe a patient.

### 4.1 Linear homogeneous growth: the graph vanishes from the lump

When every node grows at the same linear rate and transfer is conservative, the lumped burden is independent of the edge set. Two anatomies — lung-first filter-flow versus liver/bone skip-path — produced lumped trajectories that agree to RMSE \(1.289\times 10^{-8}\) (maximum absolute difference \(4.22\times 10^{-8}\)). Both agree with the closed form \(y(t)=e^{0.08 t}\) to RMSE \(3.94\times 10^{-8}\). Site-wise RMSE between the same pair is 1.68 (maximum absolute difference 7.19). At \(t=40\) the filter-flow occupancy is concentrated on liver (8.33) and bone (8.22), with lung 3.31 and primary 2.11. The skip-path occupancy is concentrated on lung (10.50) and brain (6.96), with primary 0.69. The first site to cross \(\tau=0.05\) is lung at \(t=0.5\) on the filter-flow graph and liver at \(t=1.0\) on the skip-path graph.

**Table 4-1.** Experiment 1: linear homogeneous growth, filter-flow versus skip-path.

| Contrast | Value |
| --- | --- |
| Lumped RMSE (filter vs skip) | \(1.289\times 10^{-8}\) |
| Lumped RMSE vs \(y=y_0 e^{rt}\) | \(3.937\times 10^{-8}\) |
| Site-wise RMSE | 1.677 |
| First site (filter) | lung at \(t=0.5\) |
| First site (skip) | liver at \(t=1.0\) |

The structural moral is blunt. If a laboratory observes only \(y(t)\) and growth is homogeneous, *every* conservative \(W\) is a pre-image of the same output. The graph is not a small perturbation of a local ODE. It is invisible.

### 4.2 Logistic-soil twins: matched lump, different anatomy

Heterogeneous carrying capacities and growth rates (soil) couple the lump to the distribution: \(\dot y = \sum_i r_i x_i(1-x_i/K_i)\). The lump can therefore *see* a mixture of soil and routing. That does not identify either factor. A skip-path twin was fitted to the filter-flow lumped sum. Lumped RMSE after the fit is \(2.27\times 10^{-4}\) (relative RMSE \(6.29\times 10^{-6}\); final lumped burdens 115.360 versus 115.359). Site-wise RMSE remains 10.66. Primary-only RMSE is 9.25: even the primary coordinate of the “same” lump is a different trajectory. Final filter-flow mass sits mainly on primary (50.95) and lung (27.78); the skip twin sits mainly on liver (47.58) and primary (34.46), with lung only 5.07. First detectable site is lung at \(t=1.5\) versus liver at \(t=0.5\).

**Table 4-2.** Experiment 2: logistic-soil twins fitted on the lumped sum.

| Contrast | Filter-flow | Skip-path twin |
| --- | --- | --- |
| Lumped RMSE versus twin | — | \(2.27\times 10^{-4}\) |
| Site-wise RMSE versus twin | — | 10.66 |
| First detectable site | lung, \(t=1.5\) | liver, \(t=0.5\) |
| Final \(x_P, x_L, x_V\) | 50.95, 27.78, 17.11 | 34.46, 5.07, 47.58 |
| Final lumped \(y\) | 115.360 | 115.359 |

A laboratory that reports a “metastasis parameter” from \(y(t)\) has named a mixture. It has not named a route.

Sliding the lung-share \(\alpha\) of a *fixed* total primary shedding, without retuning soil, does *not* leave the lump invariant (Experiment 4): lumped SSE versus the lung-only reference ranges from 0 at \(\alpha=1\) to 3555 at \(\alpha=0\), while site-wise SSE ranges from 0 to \(3.68\times 10^4\). Heterogeneous soil makes the lump a blurred mixture, not a complete knockout and not an identifier. The twins of Experiment 2 are the relevant object: once \(r\) and \(K\) are allowed to compensate, the lump can be matched and the anatomy can still flip.

### 4.3 Fisher information ranks under four maps

Six skip-path edge rates were ranked from local sensitivities.

**Table 4-3.** Finite-difference Fisher information ranks on six edge rates.

| Observation map | \(n_{\mathrm{obs}}\) | Numerical rank / 6 | \(\lambda_{\max}\) | \(\lambda_{\min>0}\) | \(\log_{10}\kappa\) |
| --- | --- | --- | --- | --- | --- |
| Lumped sum | 81 | 5 / 6 | \(8.35\times 10^{7}\) | \(4.30\times 10^{-2}\) | 9.29 |
| Primary only | 81 | 4 / 6 | \(1.56\times 10^{7}\) | \(3.37\times 10^{-11}\) | 17.66 |
| Lesion-count analogue | 81 | 1 / 6 | — | — | — |
| Full site-wise state | 405 | 6 / 6 | \(1.24\times 10^{8}\) | \(1.62\times 10^{4}\) | 3.88 |

The lumped sum does not give a full-rank, well-conditioned information matrix on six edges: one direction is numerically null and the remaining spectrum is sloppy by nine orders of magnitude. Primary volume is worse (rank 4, \(\log_{10}\kappa\approx 17.7\)). A thresholded lesion-count analogue collapses to rank 1; a step-valued count is almost insensitive to continuous rates. The full site-wise state restores rank 6 and drops the condition number by more than five orders of magnitude relative to the lump. That restoration is exactly a change of observation map. It is not a rehabilitation of Class A.

These ranks are local and noise-free. Practical identifiability with realistic assay noise would be stricter [37,41,42]. They are already enough to refuse the sentence “the lumped burden identified the edges.”

### 4.4 Occupancy waiting times versus first-site identity

A binary occupancy chain with matched total primary shedding produces nearly interchangeable first-event clocks and incompatible first-site identities.

**Table 4-4.** Occupancy-chain first-event times versus first-site counts (4000 paths).

| Statistic | Filter-flow | Skip-path (rate-matched) |
| --- | --- | --- |
| Mean waiting time | 9.67 | 9.86 |
| Median waiting time | 6.55 | 6.97 |
| KS statistic on waiting times | 0.028 | 0.028 |
| First-site counts L, V, B, R | 3175, 210, 395, 220 | 827, 2343, 624, 206 |
| Modal first site | lung | liver |

A DMFS-like curve is a functional of the waiting-time law [42]. Table 4-4 is the toy form of Álvarez-Arenas’ warning: the clock can be matched while the node that rang it is not. Newton’s breast-cancer analysis treated first site as a state that structures the rest of the walk [28]. A lumped event time discards that state.

### 4.5 Spreader and sponge roles are undefined on \(T(t)\)

On a toy four-site matrix, lung is a spreader (\(P_{\mathrm{out}}/P_{\mathrm{in}}=1.82\)); liver, bone and brain are sponges (0.74, 0.95, 0.95).

**Table 4-5.** Spreader / sponge roles on a toy transition matrix.

| Site | \(P_{\mathrm{in}}\) | \(P_{\mathrm{out}}\) | \(P_{\mathrm{out}}/P_{\mathrm{in}}\) | Role |
| --- | --- | --- | --- | --- |
| Lung | 0.55 | 1.00 | 1.818 | spreader |
| Liver | 1.35 | 1.00 | 0.741 | sponge |
| Bone | 1.05 | 1.00 | 0.952 | sponge |
| Brain | 1.05 | 1.00 | 0.952 | sponge |

The ratio is a function of \(P\) [27,28]. A scalar \(T(t)\) has no \(P_{\mathrm{in}}\) and no \(P_{\mathrm{out}}\). Reporting a spreader organ from a lumped burden is a type error. Reporting it as a treatment target is Gate 0 [54].

### 4.6 A Class A logistic can describe a graph lump

A two-parameter logistic fitted to the filter-flow lumped sum of Experiment 2 returns \(\hat r=0.1575\), \(\hat K=141.49\), lumped RMSE 1.026. Relative to a final burden of 115, that is about one percent. The skip-path *graph* twin of Experiment 2 matches the same lump far more tightly (RMSE \(2.27\times 10^{-4}\)) and is still the wrong anatomy. Both facts can be true at once: Class A can be an adequate *curve-fitter* for \(y(t)\), and remain inadequate for every graph question in Table 3-2. That is Gerlee’s model muddle moved one spatial scale up [15,16].

### 4.7 Synthesis: what stays unidentified

**Table 4-6.** Graph observables that remain unidentified under lumped outputs.

| Observable | Why the lump does not identify it | Support in this repository |
| --- | --- | --- |
| Occupancy vector \(\sigma\) / seeded set | Any permutation of mass with the same sum | Exp. 1, 2: site RMSE ≫ lumped RMSE |
| First-site identity | Distinct first nodes can share a clock | Exp. 1, 2, 5 |
| Transition matrix / edge rates | \(O(\|E\|)\) symbols; lumped \(y\) is one channel; FIM sloppy or rank-deficient | Exp. 3; Newton underdetermination [26,32] |
| Spreader vs sponge | Ratio of in- and out-flow on \(P\) | Exp. 6; undefined on \(T(t)\) |
| Transit times / waiting-time laws | Event times keep a clock and lose the edge | Exp. 5; stage-as-time is relative [32] |
| Organ-specific soil \(r_i,K_i\) | Mixed with routing in \(\dot y\) | Exp. 2, 4 |
| Direct vs secondary seeding \(\lambda\) vs \(\varphi\) | Occult intermediates inflate apparent primary-to-distant rates [30–32] | Filter-flow construction; not split by \(y\) |
| Self-seeding flux | Extra primary growth vs return edge vs secondary-driven return [30,33–35] | Class B definition; refused as a local \(\theta\) |
| Occult micrometastatic occupancy | Invisible to maps with threshold \(\tau\) [12,13] | Detection-floor maps in Table 3-2 |
| Historical path / phylogeny | Which edges were used [43,44] | Not supplied by any \(\Phi\) in Table 3-2 |

“Unidentified” means: not uniquely determined by \(\Phi\), even in the noise-free structural sense, unless extra structure (anatomical sparsity, a time proxy, site-resolved data, phylogeny) is added and declared [32,36–42]. Adding those measurements changes the observation map. It does not license a clinical product [54].

---

# CHAPTER FIVE

## 5.0 DISCUSSION, CONCLUSION AND RECOMMENDATION

### 5.1 Discussion

The anatomical-graph literature does not abolish local growth laws. It changes the question those laws are allowed to answer. Volume series remain the right objects for comparing Gompertz against logistic in a xenograft [15,16]. They are the wrong objects for claiming that organotropism, first-site identity, or secondary seeding has been identified.

Chapter Four makes that sentence numerical on a cartoon that is allowed to be cartoonish. Experiment 1 is the clean structural case: homogeneous linear growth plus conservative transfer, and the lump is exactly the local ODE \( \dot y = r y \) for every graph. Experiment 2 is the dishonest-looking case that a modeller will actually meet: soil is heterogeneous, the lump *can* be fitted, and the anatomy underneath can still be lung-first or liver-first. Experiment 3 says the same thing in the language of Fisher geometry: site-wise outputs buy rank and condition; lumped outputs spend it. Experiment 5 says it in the language of DMFS: matched clocks, unmatched nodes. Experiment 7 says it in the language of Class A: a logistic will happily describe a graph lump and remain mute.

The honest remainder is large. Autopsy histograms are end-of-life, not trajectories, and Newton’s series is untreated and historically dated [25–27]. Claims networks mix coding practice with biology [24]. Stage is a crude clock [32]. Filter-flow abstracts capillary beds as filters and does not identify soil coefficients [31]. Binary occupancy ignores colony size; Iwata-type size distributions ignore organ identity [18,32]. Phylogenies are still rare relative to imaging [43,44]. Practical identifiability of even two scalars from DMFS is fragile [42]. The toy five-node graph ignores skip-metastases, treatment, immune clearance, and every hallmark that is not a rate [11]. Those limits are reasons to keep symbols unidentified, not reasons to collapse back to a local ODE and speak as if the graph had been seen.

This thesis does not compete with theses 01–04. Those documents fence knowledge-to-parameter promotion, guideline-to-coefficient promotion, chart-to-profile promotion, and occult-to-continuous-\(\Theta\) promotion [49–52]. This document fences lumped-burden-to-anatomical-graph promotion. A laboratory can obey all five fences at once: refuse OnCo as \(\Theta\), refuse NSTG as a rate, refuse a profile as CDS, refuse occult as a hidden coordinate, and refuse a summed volume as a transition matrix.

CONFLUENCE’s 15-dimensional local state does not change the test. Fifteen local coordinates are not \(n\) organ nodes. Enlarging \(d\) without changing \(\Phi\) does not identify \(P\) [48,49].

Limitations of this study, stated so they cannot be skipped:

- The laboratory is a five-node cartoon with seed 5. It is not Newton’s 50-site autopsy chain and not a 446-patient breast-cancer series [26–28].
- Fisher ranks are local finite-difference ranks, not Gröbner-basis structural certificates and not profile-likelihood intervals [37–41].
- Literature models disagree on state (walker versus binary occupancy versus size density versus spatial grid). Table 4-6 is the union of what lumped maps hide; it is not a claim that one representation is true.
- CONFLUENCE, OnCo, NSTG, and Disease Profiles are neighbouring artefacts. They are not materials of a graph fit.
- Clinical datasets cited from other groups (SEER ovarian, Memorial Sloan Kettering breast, untreated autopsy, Medicare claims, UROCCR DMFS) are not re-analysed here and are not a validation of this thesis as a product [24,25,28,32,42].
- This document has no DOI.

### 5.2 Conclusion

The aim of this research was to ask whether a local tumour-burden ODE remains an adequate in-silico object once dissemination is written as spreading on an organ-to-organ anatomical graph, or whether graph observables stay unidentified under lumped outputs. The study concludes that:

i. A Class A model is adequate only for questions that do not change when the anatomical path behind a lumped output is swapped [15,16,36–41].
ii. Under homogeneous linear growth, conservative transfers are structurally invisible to \(y=\sum x_i\) (lumped RMSE \(1.3\times 10^{-8}\); first sites lung versus liver).
iii. Under logistic soil, a second anatomy can be fitted to the same lump (relative RMSE \(6.3\times 10^{-6}\)) while site-wise RMSE remains 10.66 and first-site identity flips.
iv. Finite-difference Fisher information on six edge rates is rank-deficient or sloppy from lumped and primary maps, and full-rank only after the observation map becomes site-wise.
v. Occupancy waiting times can be matched (KS 0.028) while first-site histograms cannot (lung 3175 vs liver 2343 in 4000 paths).
vi. Spreader/sponge roles, self-seeding flux, secondary seeding, occult occupancy, and phylogenetic path stay unidentified under primary volumes, summed burdens, lesion counts, and DMFS-like clocks [21,26–28,30–32,42–44].
vii. Scientific success for this thesis is that typed remainder, not disease eradication [2,54].

This work is computational research. It is not a medical device, not CDS, not a dose, and not a cure. It is not the 2022 wet-lab *Carica papaya* AgNP antidiabetic project. It is not a treatment of metastasis [54].

### 5.3 Recommendation

The following recommendations follow from the gates, not from a clinic:

i. Before writing a “metastasis parameter” into a local ODE, name the observation map and the question. If the question is not invariant under lumped-equivalent graph trajectories, change the map or refuse the parameter [36–41].
ii. Keep filter-flow anatomy as a sparsity constraint (knowledge), not as personalized therapy [31,54].
iii. Do not treat spreader/sponge diagrams as targeting lists [27,28,54].
iv. If a later worker estimates edge rates, report them with anatomical sparsity, a declared time proxy, site-resolved occupancy, and uncertainty; relative rates from stage are not calendar-time rates [32].
v. Re-run `scripts/identifiability_experiment.py` when the toy graph is extended; do not quote Chapter Four as a human result.
vi. Optional later: deposit this PDF on Zenodo or a preprint server and only then add a document DOI to `CITATION.cff`.
vii. Translation (Gate 8) should remain out of scope until biological and clinical validation that this repository does not claim [2,54].

---

## REFERENCES

Journal items use Vancouver form. DOI fields appear only for Crossref- or PubMed-verified journal records. WHO and GitHub items are complete Internet citations without a `doi:` field. No DOI is invented. This document has no registered DOI.

1. Sung H, Filho AM, Laversanne M, Ferlay J, Siegel RL, Soerjomataram I, et al. Global cancer statistics 2024: GLOBOCAN estimates of incidence and mortality worldwide for 34 cancers in 186 countries. CA Cancer J Clin. 2026;76(4):e70090. doi:10.3322/caac.70090.
2. World Health Organization. Cancer [Internet]. Geneva: World Health Organization; 2026 [cited 2026 Sep 21]. Available from: https://www.who.int/news-room/fact-sheets/detail/cancer
3. Paget S. The distribution of secondary growths in cancer of the breast. Lancet. 1889;133(3421):571-573. doi:10.1016/S0140-6736(00)49915-0.
4. Fidler IJ. The pathogenesis of cancer metastasis: the 'seed and soil' hypothesis revisited. Nat Rev Cancer. 2003;3(6):453-458. doi:10.1038/nrc1098.
5. Chambers AF, Groom AC, MacDonald IC. Dissemination and growth of cancer cells in metastatic sites. Nat Rev Cancer. 2002;2(8):563-572. doi:10.1038/nrc865.
6. Gupta GP, Massagué J. Cancer metastasis: building a framework. Cell. 2006;127(4):679-695. doi:10.1016/j.cell.2006.11.001.
7. Nguyen DX, Bos PD, Massagué J. Metastasis: from dissemination to organ-specific colonization. Nat Rev Cancer. 2009;9(4):274-284. doi:10.1038/nrc2622.
8. Valastyan S, Weinberg RA. Tumor metastasis: molecular insights and evolving paradigms. Cell. 2011;147(2):275-292. doi:10.1016/j.cell.2011.09.024.
9. Obenauf AC, Massagué J. Surviving at a distance: organ-specific metastasis. Trends Cancer. 2015;1(1):76-91. doi:10.1016/j.trecan.2015.07.009.
10. Lambert AW, Pattabiraman DR, Weinberg RA. Emerging biological principles of metastasis. Cell. 2017;168(4):670-691. doi:10.1016/j.cell.2016.11.037.
11. Hanahan D, Weinberg RA. Hallmarks of cancer: the next generation. Cell. 2011;144(5):646-674. doi:10.1016/j.cell.2011.02.013.
12. Klein CA. Parallel progression of primary tumours and metastases. Nat Rev Cancer. 2009;9(4):302-312. doi:10.1038/nrc2627.
13. Aguirre-Ghiso JA. Models, mechanisms and clinical evidence for cancer dormancy. Nat Rev Cancer. 2007;7(11):834-846. doi:10.1038/nrc2256.
14. Laird AK. Dynamics of tumor growth. Br J Cancer. 1964;18(3):490-502. doi:10.1038/bjc.1964.55.
15. Gerlee P. The model muddle: in search of tumor growth laws. Cancer Res. 2013;73(8):2407-2411. doi:10.1158/0008-5472.CAN-12-4355.
16. Benzekry S, Lamont C, Beheshti A, Tracz A, Ebos JML, Hlatky L, et al. Classical mathematical models for description and prediction of experimental tumor growth. PLoS Comput Biol. 2014;10(8):e1003800. doi:10.1371/journal.pcbi.1003800.
17. Altrock PM, Liu LL, Michor F. The mathematics of cancer: integrating quantitative models. Nat Rev Cancer. 2015;15(12):730-745. doi:10.1038/nrc4029.
18. Iwata K, Kawasaki K, Shigesada N. A dynamical model for the growth and size distribution of multiple metastatic tumors. J Theor Biol. 2000;203(2):177-186. doi:10.1006/jtbi.2000.1075.
19. Barbolosi D, Benabdallah A, Hubert F, Verga F. Mathematical and numerical analysis for a model of growing metastatic tumors. Math Biosci. 2009;218(1):1-14. doi:10.1016/j.mbs.2008.11.008.
20. Hartung N, Mollard S, Barbolosi D, Benabdallah A, Chapuisat G, Henry G, et al. Mathematical modeling of tumor growth and metastatic spreading: validation in tumor-bearing mice. Cancer Res. 2014;74(22):6397-6407. doi:10.1158/0008-5472.CAN-14-0721.
21. Baratchart E, Benzekry S, Bikfalvi A, Colin T, Cooley LS, Pineau R, et al. Computational modelling of metastasis development in renal cell carcinoma. PLoS Comput Biol. 2015;11(11):e1004626. doi:10.1371/journal.pcbi.1004626.
22. Benzekry S, Tracz A, Mastri M, Corbelli R, Barbolosi D, Ebos JML. Modeling spontaneous metastasis following surgery: an in vivo-in silico approach. Cancer Res. 2016;76(3):535-547. doi:10.1158/0008-5472.CAN-15-1389.
23. Franssen LC, Lorenzi T, Burgess AEF, Chaplain MAJ. A mathematical framework for modelling the metastatic spread of cancer. Bull Math Biol. 2019;81(6):1965-2010. doi:10.1007/s11538-019-00597-x.
24. Chen LL, Blumm N, Christakis NA, Barabási AL, Deisboeck TS. Cancer metastasis networks and the prediction of progression patterns. Br J Cancer. 2009;101(5):749-758. doi:10.1038/sj.bjc.6605214.
25. DiSibio G, French SW. Metastatic patterns of cancers: results from a large autopsy study. Arch Pathol Lab Med. 2008;132(6):931-939. doi:10.5858/2008-132-931-MPOCRF.
26. Newton PK, Mason J, Bethel K, Bazhenova LA, Nieva J, Kuhn P. A stochastic Markov chain model to describe lung cancer growth and metastasis. PLoS One. 2012;7(4):e34637. doi:10.1371/journal.pone.0034637.
27. Newton PK, Mason J, Bethel K, Bazhenova L, Nieva J, Norton L, et al. Spreaders and sponges define metastasis in lung cancer: a Markov chain Monte Carlo mathematical model. Cancer Res. 2013;73(9):2760-2769. doi:10.1158/0008-5472.CAN-12-4488.
28. Newton PK, Mason J, Venkatappa N, Jochelson MS, Hurt B, Nieva J, Comen E, Norton L, Kuhn P. Spatiotemporal progression of metastatic breast cancer: a Markov chain model highlighting the role of early metastatic sites. npj Breast Cancer. 2015;1:15018. doi:10.1038/npjbcancer.2015.18.
29. Scott J, Kuhn P, Anderson ARA. Unifying metastasis — integrating intravasation, circulation and end-organ colonization. Nat Rev Cancer. 2012;12(7):445-446. doi:10.1038/nrc3287.
30. Scott JG, Basanta D, Anderson ARA, Gerlee P. A mathematical model of tumour self-seeding reveals secondary metastatic deposits as drivers of primary tumour growth. J R Soc Interface. 2013;10(82):20130011. doi:10.1098/rsif.2013.0011.
31. Scott JG, Fletcher AG, Maini PK, Anderson AR, Gerlee P. A filter-flow perspective of haematogenous metastasis offers a non-genetic paradigm for personalised cancer therapy. Eur J Cancer. 2014;50(17):3068-3075. doi:10.1016/j.ejca.2014.08.019.
32. Gerlee P, Johansson M. Inferring rates of metastatic dissemination using stochastic network models. PLoS Comput Biol. 2019;15(4):e1006868. doi:10.1371/journal.pcbi.1006868.
33. Norton L, Massagué J. Is cancer a disease of self-seeding? Nat Med. 2006;12(8):875-878. doi:10.1038/nm0806-875.
34. Kim MY, Oskarsson T, Acharyya S, Nguyen DX, Zhang XHF, Norton L, et al. Tumor self-seeding by circulating cancer cells. Cell. 2009;139(7):1315-1326. doi:10.1016/j.cell.2009.11.025.
35. Comen E, Norton L, Massagué J. Clinical implications of cancer self-seeding. Nat Rev Clin Oncol. 2011;8(6):369-377. doi:10.1038/nrclinonc.2011.64.
36. Bellman R, Åström KJ. On structural identifiability. Math Biosci. 1970;7(3-4):329-339. doi:10.1016/0025-5564(70)90132-X.
37. Raue A, Kreutz C, Maiwald T, Bachmann J, Schilling M, Klingmüller U, et al. Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood. Bioinformatics. 2009;25(15):1923-1929. doi:10.1093/bioinformatics/btp358.
38. Chis OT, Banga JR, Balsa-Canto E. Structural identifiability of systems biology models: a critical comparison of methods. PLoS One. 2011;6(11):e27755. doi:10.1371/journal.pone.0027755.
39. Villaverde AF, Barreiro A, Papachristodoulou A. Structural identifiability of dynamic systems biology models. PLoS Comput Biol. 2016;12(10):e1005153. doi:10.1371/journal.pcbi.1005153.
40. Villaverde AF. Observability and structural identifiability of nonlinear biological systems. Complexity. 2019;2019:8497093. doi:10.1155/2019/8497093.
41. Wieland FG, Hauber AL, Rosenblatt M, Tönsing C, Timmer J. On structural and practical identifiability. Curr Opin Syst Biol. 2021;25:60-69. doi:10.1016/j.coisb.2021.03.005.
42. Álvarez-Arenas A, Souleyreau W, Emanuelli A, Cooley LS, Bernhard JC, Bikfalvi A, et al. Practical identifiability analysis of a mechanistic model for the time to distant metastatic relapse and its application to renal cell carcinoma. PLoS Comput Biol. 2022;18(8):e1010444. doi:10.1371/journal.pcbi.1010444.
43. Naxerova K, Jain RK. Using tumour phylogenetics to identify the roots of metastasis in humans. Nat Rev Clin Oncol. 2015;12(5):258-272. doi:10.1038/nrclinonc.2014.238.
44. Gundem G, Van Loo P, Kremeyer B, Alexandrov LB, Tubio JMC, Papaemmanuil E, et al. The evolutionary history of lethal metastatic prostate cancer. Nature. 2015;520(7547):353-357. doi:10.1038/nature14347.
45. Gatenby RA, Silva AS, Gillies RJ, Frieden BR. Adaptive therapy. Cancer Res. 2009;69(11):4894-4903. doi:10.1158/0008-5472.CAN-08-3658.
46. Ogbonna KE. identifiability_results.json [Internet]. Thesis #5 / GitHub; 2026 Sep 21 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs/blob/main/results/identifiability_results.json
47. Ogbonna KE. identifiability_experiment.py [Internet]. Thesis #5 / GitHub; 2026 Sep 21 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs/blob/main/scripts/identifiability_experiment.py
48. Ogbonna KE. Project Confluence [Internet]. GitHub; 2026 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/project-confluence
49. Ogbonna KE. CONFLUENCE × OnCo: an evidence-gated dynamical framework for integrating oncology knowledge graphs with adaptive cancer-state models [Internet]. Thesis #1 computational research thesis. September 2026 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/thesis-01-confluence-onco
50. Ogbonna KE. Complexity science and NSTG-guided in-silico pathology dynamics for biologics pathway exploration [Internet]. Thesis #2 working manuscript. 20 September 2026 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/thesis-02-complexity-nstg
51. Ogbonna KE. Disease profiles for complex pathologies: a gated method for systemic personalized-medicine research objects [Internet]. Thesis #3 working manuscript. 20 September 2026 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/thesis-03-disease-profile
52. Ogbonna KE. Occult residual disease as a hybrid switching system: named modes, switching observables, and a refusal to smuggle continuous Θ [Internet]. Thesis #4 working manuscript. 21 September 2026 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/thesis-04-occult-hybrid-switching
53. Ogbonna KE. NEXT_PAPERS.md [Internet]. Research Theses Hub / GitHub; 2026 Sep 21 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/research-theses-hub/blob/main/NEXT_PAPERS.md
54. Ogbonna KE. DISCLAIMER.md [Internet]. Thesis #5 / GitHub; 2026 Sep 21 [cited 2026 Sep 21]. Available from: https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs/blob/main/DISCLAIMER.md

---

## Disclaimer

**Research technical report.** This repository is a computational research manuscript. It is not a medical device, not a clinical decision-support system, not a diagnostic or therapeutic product, and not a protocol [54]. This document makes no cure claim, no dosing recommendation, and no claim of patient benefit [2,54]. Simulated trajectories are not patient outcomes. Current results are computational unless an external experiment is cited.

Dedicated deposit: https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs
Hub index: https://github.com/cloudynirvana/research-theses-hub
