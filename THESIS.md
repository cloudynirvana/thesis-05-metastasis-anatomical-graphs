# Metastasis as Stochastic Spreading on Organ-to-Organ Anatomical Graphs: Adequacy of Local Tumour-Burden ODEs under Lumped Outputs

**Document type:** Thesis #5 — working manuscript (computational research)
**Author:** Kelechi Emeka Ogbonna
**Affiliation:** Independent computational research / Project Confluence (GitHub cloudynirvana)
**Correspondence:** kelechiogbonna300@gmail.com · https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs
**Date:** 21 September 2026
**Status:** Methodological identifiability argument. Not a clinical result. Not a metastasis-treatment claim.
**Citation style:** numbered Vancouver [n] matching the References list in `refs/references.md`.
**DOI:** none registered for this document. Do not invent one.

This manuscript is a new problem at the anatomical-network scale. It is not a restatement of theses 01–03 [47–49]. It does not add wet-lab measurements, patient-level results, or invented identifiers.

---

## Abstract

Local tumour-burden ordinary differential equations (ODEs) treat disease as a scalar, or a small vector, attached to one site. Metastasis, as written in the anatomical-network literature, is a stochastic process on a directed graph whose nodes are organs or nodal stations and whose edges are haematogenous or lymphatic routes [24,26–32]. This thesis asks whether the local ODE remains an adequate in-silico object once that graph is admitted, or whether graph observables remain unidentified under the lumped outputs that current burden models actually see.

The methods contrast two model classes without fitting a new cohort. Class A is a local growth law — Gompertz, logistic, Gomp-Exp, or a lumped multi-compartment cancer-state ODE — observed through primary volume, a summed metastatic burden, a serum marker, or a distant-metastasis-free survival (DMFS) curve [14–16,18–22,42]. Class B is spreading on an organ-to-organ graph: a Markov random walk, a binary occupancy chain, or a filter-flow network constrained by capillary beds [24,26–32]. Identifiability is used as a refusal rule, not as a new numerical certificate [36–42].

Under lumped outputs the following stay unidentified: the occupancy vector (which organs are seeded), first-site identity, the transition matrix, spreader versus sponge roles, transit times, organ-specific colonization, the split between primary shedding and secondary seeding, and self-seeding flux [26–32,33–35,42]. Newton and colleagues had to assume a steady-state match to autopsy frequencies because the walk was underdetermined [26,27,32]. Gerlee and Johansson recovered relative, anatomically constrained rates only after adding stage as a time proxy and forbidding skip-edges; even then the rates are not calendar-time parameters [32]. Hartung and colleagues found peritoneal metastatic growth that an ODE could not describe [20]. Baratchart and colleagues could match total metastatic burden while the size distribution of colonies remained wrong until spatial merging was added [21]. Álvarez-Arenas and colleagues showed that even a two-parameter growth-and-dissemination model is not practically identifiable from a DMFS curve unless the fraction with metastasis at diagnosis is supplied [42].

GLOBOCAN 2024 estimates, published 2026, place the contemporary burden at about 20.6 million diagnoses and 9.8 million deaths [1]. That statistic motivates computational work on dissemination. It is not a graph parameter and not a product claim [2,50]. This document does not claim a treatment of metastasis, a targeting list for “spreader” organs, a personalized filter-flow protocol, or an identified Θ [31,50]. Scientific success here is a typed distinction between lumped burden and graph observables, with unidentified symbols left labelled as such [36–41].

---

## Keywords

computational oncology; metastasis; anatomical graphs; Markov chains; identifiability; lumped outputs; tumour-burden ODE; seed and soil; filter-flow; research-only; not a medical device

---

## Introduction

A local tumour-burden ODE answers how much tissue is present, at one site or as a sum, as a function of time [14–17]. Metastasis answers a different question: which organs are occupied, in what order, along which routes, and with what waiting times [5–10,24,26–32]. Collapsing the second question into the first treats a scalar as a sufficient statistic for a directed anatomical network.

Paget’s 1889 seed-and-soil remark, Ewing’s later mechanical alternative, and the modern cascade reviews agree on one empirical fact even when they disagree on mechanism: secondary growth is organ-patterned, inefficient, and often occult at the scale of a clinical scan [3–10,12,13]. Circulating cells are numerous; colonies are rare [5,6]. Parallel progression and dormancy further imply that a late, lumped burden can hide an earlier occupancy pattern [12,13]. None of those reviews identifies a coefficient in a local ODE.

Two modelling traditions now sit side by side. One continues the classical growth-law programme: Laird’s Gompertz observation, Gerlee’s warning that growth laws are under-determined by bulk curves, Benzekry and colleagues’ comparison of ODE families on experimental volume series, and the Iwata transport equation for a size distribution of metastases that is still spatially unresolved [14–18]. The other treats organs as nodes and dissemination as a walk or an occupancy process on a graph built from claims data, autopsy series, or anatomical flow [24–32]. Chen and colleagues introduced metastasis networks from Medicare co-occurrence [24]. Newton and colleagues fitted Markov chains to untreated autopsy frequencies and, later, to a longitudinal breast-cancer series [25–28]. Scott, Kuhn, Anderson, Gerlee and colleagues wrote haematogenous spread as filter-flow through successive capillary beds and showed that self-seeding of the primary, as a growth driver, requires secondary deposits [29–31]. Gerlee and Johansson then replaced Newton’s steady-state assumption with a temporal, anatomically constrained occupancy model [32].

The failure mode this thesis names is not that either tradition is empty. It is that a laboratory can keep a local ODE, observe only a lumped output, and still speak as if seeded sites, routes, and organ-specific colonization had been identified. Structural identifiability asks whether a unique parameter vector is consistent with noise-free input–output data [36–40]. Practical identifiability asks whether finite, noisy data actually constrain those parameters [37,41,42]. A lumped map \(y(t)=\sum_i x_i(t)\), or a primary-only volume, or a DMFS curve, is a many-to-one observation of a graph process. Many-to-one maps hide coordinates. The coordinates that stay hidden are the subject of this manuscript.

GLOBOCAN 2024 estimates (about 20.6 million diagnoses and 9.8 million deaths across 34 cancers and 186 countries) are setting context [1,2]. They are not CONFLUENCE parameters, not edge weights, and not a licence to treat [50]. WHO language that many cancers can be cured if found early and treated well is a health-system statement about staged, treatable disease [2]. It is not a claim that an anatomical-graph model treats metastasis.

---

## 1. Problem Statement

Does a local tumour-burden ordinary differential equation remain an adequate in-silico object once dissemination is posed as a stochastic process on an organ-to-organ anatomical graph, or do graph observables remain unidentified under current lumped outputs [15–18,24,26–32,36–42]?

That is the research problem. It is a computational and medical-methods problem. It is not a claim to treat, dose, resect, irradiate, or otherwise manage metastatic disease [2,31,50].

A local burden model — Gompertz, logistic, Bertalanffy, a Gomp-Exp splice, the Iwata colony-size transport equation closed by a shedding boundary, or a lumped multi-compartment cancer-state ODE — is built to track how much tumour is present [14–22]. Its natural outputs are volumes, summed burdens, and, at one further remove, time-to-event curves derived from a detection threshold [20–22,42]. An anatomical-graph model is built to track where tumour is present. Its state is an occupancy vector or a site-wise burden on a directed network whose edges are vessels, lymphatics, or empirically scored co-occurrence links [24,26–32]. Self-seeding, primary reseeding, and metastasis-to-metastasis reseeding are distinct walks on that network, not synonyms for a larger scalar [27,30,33–35].

The two objects coincide only for questions that are invariant under every graph trajectory sharing the same lumped output. Questions about first-site identity, subsequent path, spreader versus sponge roles, organ-specific colonization, and the split between direct and secondary seeding are not invariant [26–28,32]. Newton’s autopsy chain was underdetermined until a steady-state assumption was imposed [26,27,32]. A DMFS curve does not identify growth and dissemination as a pair unless further summary statistics are supplied [42]. Total metastatic burden can be described while the size distribution of colonies remains unidentified [21]. Those are identifiability facts already in the literature. The problem is to keep them attached to the lumped observation map, so that a local ODE is not silently promoted to a dissemination model.

Success is a typed distinction and a labelled list of unidentified graph observables. Success is not a survival difference, not a targeting order of organs, and not an identified Θ [36–41,50].

---

## 2. Justification of the Study

Existing modelling habits fail in documented ways that this study is built to catch.

**Overclaiming.** GLOBOCAN burden figures and WHO early-detection language are health-system context [1,2]. They are not edge weights. Mathematical oncology supplies in-silico laboratories for growth, resistance, and control [17]; adaptive-therapy papers treat dosing as a selection process in a local competitive ecology [45]. Neither literature identifies an organ-to-organ transition matrix, and neither is cited here as a metastasis-treatment protocol [45,50]. Scott and colleagues titled a filter-flow paper as a “non-genetic paradigm for personalised cancer therapy” [31]. This thesis takes the anatomical constraint from that paper — successive capillary beds as filters — and refuses the therapy claim. Newton and colleagues noted that spreader/sponge classification might later inform oligometastatic targeting [28]. That sentence is a motivation in their discussion. It is not a result of this manuscript and not a care recommendation [50].

**Lumped-output smuggling.** A primary volume series identifies, at best, a growth-law family, and even that family is not unique: Gerlee called the situation a model muddle [15]; Benzekry and colleagues showed that several classical ODEs can describe the same experimental curves [16]. Iwata, Kawasaki and Shigesada replaced a single volume with a size distribution of metastatic colonies still living in an unresolved spatial domain [18]. Subsequent analysis and mixed-effects fits can recover shedding and growth from total burden in mice and still fail the size distribution unless foci interact [19–21]. Álvarez-Arenas and colleagues reduced metastasis to two scalars, a growth rate \(\alpha\) and a dissemination rate \(\mu\), and showed that a DMFS curve does not practically identify the pair without the fraction of patients already metastatic at diagnosis [42]. If two scalars are already weakly seen from a survival curve, a transition matrix on tens of organs is not seen from a single summed burden.

**Missing graph coordinates.** Chen and colleagues showed that metastasis has a network topography in claims data [24]. DiSibio and French tabulated organ-resolved autopsy frequencies in untreated decedents [25]. Newton and colleagues turned those frequencies into a Markov chain and classified sites as spreaders or sponges [26,27]; a later breast-cancer chain made the first metastatic site as informative, in their cohort, as receptor subtype for subsequent path [28]. Gerlee and Johansson stated the underdetermination explicitly: without anatomical sparsity and a time proxy, site-to-site rates are not recoverable from incidence tables [32]. Phylogenetic studies of lethal metastatic prostate cancer show branching, reseeding, and organ-restricted clades that a scalar burden cannot encode [43,44]. Those coordinates are the gap. Theses 01–03 close other gaps — knowledge-graph provenance, guideline-as-constraint, and research-object export — and do not ask this anatomical-network question [47–49,51].

**What this study therefore does.** It writes the two model classes against one observation map, lists the graph observables that lumped outputs do not identify, and refuses to convert that list into a treatment claim [36–42,50]. It does not fit a new autopsy series or a new Markov chain.

---

## 3. Significance of the Study

**Scientific significance for researchers.** The work treats metastasis as a graph process whose state is occupancy and route, not only mass [5–10,24,26–32]. Laboratories that already run a local cancer-state ODE — including the frozen 15-dimensional CONFLUENCE lineage cited only as an example of a lumped object [46,47] — gain an explicit test: if the research question changes when two graph trajectories share the same summed burden, the local ODE is not an adequate object for that question. Unidentified symbols stay labelled [36–41].

**Methodological significance.** Identifiability literature becomes a refusal rule for anatomical networks, as it already is for knowledge-to-parameter promotion in thesis 01 [36–41,47]. The contribution is the observation map, not a new structural-identifiability algorithm and not a re-fit of Newton’s transition matrix. Efficiency, if claimed at all, is research-operational: a laboratory can ask whether it needs site-resolved occupancy, waiting times, or phylogenetic paths *before* writing another right-hand side.

**What this significance is not.** It is not clinical decision support, not a medical device, not a dose, not a cure, and not a metastasis-treatment claim [2,50]. It is not a recommendation to irradiate or resect spreader organs. It is not personalized prediction of the next metastatic site as a care product, even though Chen, Newton, and Gerlee discuss prediction inside research cohorts [24,28,32]. GLOBOCAN figures do not become colonization rates [1]. Translation after biological and clinical validation remains unclaimed. The significance of the study is methodological honesty for researchers, not a path to a clinic.

---

## Specific aims

1. State the adequacy criterion for a local tumour-burden ODE once dissemination is a graph process: invariance of the research question under lumped-equivalent trajectories [15,16,36–41].
2. Write Class A (local / spatially unresolved burden dynamics) and Class B (stochastic spreading on an organ-to-organ anatomical graph) as distinct formal objects [14–22,24,26–32].
3. Name the lumped observation maps actually used — primary volume, summed metastatic burden, detection-threshold event times, DMFS curves — and show they are many-to-one [16,20–22,42].
4. List graph observables that remain unidentified under those maps, citing the underdetermination, filter-flow, size-distribution, and DMFS identifiability results already published [21,26,27,31,32,42].
5. Refuse clinical metastasis-treatment claims, including spreader-targeted therapy, oligometastatic ablation as a consequence of a Markov diagram, and filter-flow “personalised therapy” [28,31,50].

A non-aim, stated so it cannot be inferred: this thesis does not estimate a treatment effect, does not identify a transition matrix, and does not promote CONFLUENCE, OnCo, NSTG, or a Disease Profile board into an anatomical graph [47–49].

---

## Background

### Seed, soil, filter, and cascade

Paget wrote that secondary growths are not randomly scattered [3]. Fidler restated seed-and-soil as a pathogenesis, not a slogan [4]. Chambers, Groom and MacDonald separated dissemination from colonization and documented metastatic inefficiency [5]. Gupta and Massagué, Nguyen, Bos and Massagué, Valastyan and Weinberg, Obenauf and Massagué, and Lambert, Pattabiraman and Weinberg organised the cascade from local invasion through circulation to organ-specific colonization [6–10]. Hanahan and Weinberg list activating invasion and metastasis among the hallmarks; a hallmark is not a rate constant [11]. Klein’s parallel-progression account and Aguirre-Ghiso’s dormancy review imply that occupancy can exist below a detection floor for long times [12,13]. Those statements are knowledge. They are not Θ.

Scott, Kuhn and Anderson proposed unifying haematogenous metastasis as successive filtration through capillary beds rather than as a single genetic switch [29]. Scott, Fletcher, Maini, Anderson and Gerlee then wrote an explicit filter-flow anatomy: venous-side cells meet lung as first filter; further arterial spread is conditional on that filter, on self-seeding, and on secondary seeding [31]. The anatomy is the usable object here. The “personalised cancer therapy” clause in their title is not adopted [31,50].

### Local growth laws and spatially unresolved metastasis

Laird described experimental tumour growth as Gompertzian [14]. Gerlee reviewed the subsequent zoo of growth laws and the inability of bulk curves to pick a unique form [15]. Benzekry and colleagues compared classical ODEs on experimental volume series [16]. Altrock, Liu and Michor surveyed quantitative cancer models more broadly, including stochastic and spatial families, without collapsing them into one scalar [17].

Iwata, Kawasaki and Shigesada wrote a transport equation for the size distribution of metastatic colonies, with a boundary condition for shedding from the primary [18]. Barbolosi and colleagues analysed that equation [19]. Hartung and colleagues fitted related mixed-effects models to bioluminescence in mice and reported peritoneal metastatic growth that ODE models could not describe [20]. Baratchart and colleagues fitted primary-plus-total-burden data in a renal-cell xenograft and then failed the MRI size distribution until neighbouring foci were allowed to merge [21]. Benzekry and colleagues coupled pre-surgical primary volume to post-surgical metastatic burden, still without an organ graph [22]. Franssen, Lorenzi, Burgess and Chaplain placed invasion and distant growth on a spatially explicit hybrid grid — a different spatial scale from organ-to-organ anatomy, and still not a lumped ODE [23]. The pattern is consistent: moving off a single volume exposes coordinates that the volume did not identify.

### Metastasis networks and Markov diagrams

Chen, Blumm, Christakis, Barabási and Deisboeck defined a cancer metastasis network on Medicare claims: nodes are primary and metastatic sites, links are co-occurrence strengths, and the network supports anterograde and retrograde prediction *inside that claims experiment* [24]. DiSibio and French reported metastatic patterns from a large autopsy series of untreated cancers, the empirical table later used by Newton [25]. Newton, Mason, Bethel, Bazhenova, Nieva, Kuhn and colleagues constructed a discrete Markov chain on that table for primary lung cancer, treating circulating cells as random walkers [26]. A follow-up Monte Carlo study classified sites as spreaders or sponges and distinguished self-seeding of the primary, reseeding of the primary from a metastasis, and reseeding among metastases [27]. In a 446-patient breast-cancer series, Newton and colleagues estimated subtype-specific transition probabilities and reported that the first metastatic site structured subsequent paths and survival in that cohort [28]. Those are research-cohort descriptions. They are not protocols.

Gerlee and Johansson replaced the steady-state assumption. They modelled nodes as binary (negative/positive), restricted flow to anatomically neighbouring stations, split primary shedding \(\lambda\) from metastatic shedding \(\varphi\), and used primary stage as a time proxy to infer *relative* rates on tongue-cancer lymphatic stations and on SEER ovarian patterns [32]. They state that Newton’s transition matrix was underdetermined from incidence alone [32]. That sentence is the justification for keeping graph parameters out of a lumped ODE.

### Self-seeding is a graph walk

Norton and Massagué asked whether cancer is a disease of self-seeding [33]. Kim and colleagues supplied mouse evidence that circulating cells can re-infiltrate a primary [34]. Comen, Norton and Massagué discussed clinical implications [35]. Scott, Basanta, Anderson and Gerlee showed, in a mathematical treatment, that self-seeding as a *driver of primary growth* requires secondary metastatic deposits; otherwise the return flux is negligible [30]. A primary-volume ODE that absorbs an extra growth term labelled “self-seeding” without a secondary-site state has smuggled a graph walk into a local parameter.

### Identifiability

Bellman and Åström defined structural identifiability [36]. Raue and colleagues distinguished structural from practical identifiability via profile likelihood [37]. Chis, Banga and Balsa-Canto compared computational tests for systems-biology models [38]. Villaverde, Barreiro and Papachristodoulou, and Villaverde’s later observability paper, treat unobservability and unidentifiability as properties of the model-plus-output pair [39,40]. Wieland and colleagues restated the distinction for current practice [41]. Álvarez-Arenas and colleagues applied practical identifiability to a mechanistic DMFS model: two parameters, growth and dissemination, are not a free lunch from a survival curve [42]. Naxerova and Jain, and Gundem and colleagues, show that reconstructing metastatic paths needs phylogeny, not a summed burden [43,44]. This thesis uses that literature as a refusal rule. It does not report a new identifiability computation.

---

## Methods

### Scope, materials, and non-claims

**Scope.** Computational research method. Bibliographic and formal. No patient-identifiable data. No new autopsy fit. No new Markov-chain estimate. No controller prior. No dose.

**Materials.**

- Published anatomical-network and Markov metastasis models [24,26–28,32].
- Filter-flow and self-seeding mathematics [29–31,33–35].
- Classical and metastatic growth-law papers, including size-distribution and mixed-effects fits [14–22].
- Identifiability and observability papers [36–42].
- Cascade and organotropism reviews used only as knowledge [3–13].
- Frozen CONFLUENCE lineage `confluence_v2_15d` named only as an example of a lumped local cancer-state ODE; it is not refit and its right-hand side is not edited [46,47].
- Theses 01–03 and the hub catalogue, cited so this problem is not collapsed into theirs [47–49,51].

**Non-claims** (repeated so they cannot be skipped). Simulated or literature-derived trajectories are computational artefacts. They are not patient outcomes, not a protocol, and not a dose [50]. Spreader/sponge is a network role in a fitted diagram [27,28]. It is not an indication. Filter-flow is an anatomical constraint [31]. It is not personalized therapy. DMFS modelling in Álvarez-Arenas et al. is a methods paper on identifiability [42]. It is not a prognostic device licensed here.

### Honesty gates

The public protocol is sequential and falsifiable. It is not a treatment path.

| Gate | Requirement |
| --- | --- |
| 0 | Research-only scope. Not a medical device. Not clinical decision support. Not a metastasis-treatment claim. [50] |
| 1 | Provenance: which paper, which cohort class (autopsy, claims, xenograft, SEER, single-centre longitudinal), which spatial scale. |
| 2 | Model class named: local burden ODE (A) or anatomical graph process (B). |
| 3 | Observation map named: primary volume, site-wise occupancy, summed burden, event time, DMFS. |
| 4 | Parameter: model id, symbol, units, estimator, uncertainty, identifiability. Unidentified ≠ established. [36–42] |
| 5 | Prediction labelled as computational. |
| 6 | Held-out / external / baseline validation — not claimed for a new fit in this repository. |
| 7 | An experiment that could show the claim is wrong (site-resolved occupancy, waiting times, or phylogeny that splits lumped-equivalent trajectories). |
| 8 | Translation only after biological and clinical validation this repository does not claim. [2,50] |

Scientific success is: traceability → mathematical validity → identifiability → labelled unidentified remainder. Disease eradication is not a success criterion of this thesis [2,50].

### Class A — local tumour-burden dynamics

Let \(T(t)\ge 0\) denote a local or spatially unresolved tumour burden (cells, volume, or a proxy). A typical closed ODE is
\[
\dot T = g(T;\theta),\qquad y(t)=h(T(t)),
\]
with \(g\) Gompertz, logistic, Bertalanffy, exponential, or a Gomp-Exp splice [14–16], and \(h\) the identity, a noisy volume, or a threshold that yields an event time. Multi-compartment local models (immune, resource, lactate, hypoxia) enlarge \(T\) to a vector \(X(t)\in\mathbb{R}^d\) still attached to one site or to an unresolved sum [17,46]. They do not, by that enlargement alone, become organ graphs.

Iwata-type models replace \(T\) by a density \(u(x,t)\) of colonies of size \(x\) [18,19]:
\[
\partial_t u + \partial_x\bigl(g(x)u\bigr)=0,
\]
with a boundary flux from primary shedding. The spatial domain of \(x\) is size, not anatomy. Hartung’s report that peritoneal growth escaped an ODE description is a documented limit of Class A, not a graph identification [20]. Baratchart’s total-burden success against size-distribution failure is the same limit in a different output [21].

CONFLUENCE `confluence_v2_15d` is cited only as a lumped cancer-state ODE already fenced by thesis 01’s knowledge gates [46,47]. This thesis does not open that right-hand side and does not add organ nodes to it.

### Class B — stochastic spreading on an anatomical graph

Let \(G=(V,E)\) be a directed graph. Vertices \(V=\{1,\ldots,n\}\) are organs, nodal stations, or other anatomical compartments. Edges \(E\) are feasible routes: lymphatic drainage, venous-to-lung filter, arterial distribution, transcoelomic spread, or empirically scored links [24,29–32].

Three representations appear in the cited literature and are used here as a family, not as a newly fitted model.

1. **Markov walk.** A circulating walker has transition matrix \(P=(P_{ij})\), possibly with a death or absorption state. Site frequencies in the large-time limit are a left eigenvector if a steady state exists. Newton and colleagues estimated \(P\) from autopsy histograms under that assumption [26,27]. Occupancy of walkers at nodes yields spreader/sponge roles from in- and out-flow [27,28].

2. **Binary occupancy chain.** Each node \(i\) has state \(\sigma_i\in\{0,1\}\). A positive node sheds along outgoing edges at rates \(\lambda\) (if primary) or \(\varphi\) (if metastatic). Skip-edges are forbidden or rare. Gerlee and Johansson used this form so that the number of free parameters tracked anatomical links rather than a dense \(n\times n\) matrix [32].

3. **Filter-flow.** Haematogenous passage is a cascade of filters, not an all-to-all genetic lottery [29,31]. Apparent primary-to-distant rates mix true direct colonization with occult intermediate colonies [30,32]. Self-seeding is an edge back to the primary, not a local growth coefficient [30,33–35].

Let \(x(t)\in\mathbb{R}^n_{\ge 0}\) be site-wise burden, or \(\sigma(t)\in\{0,1\}^n\) site-wise occupancy. Dynamics are a continuous-time Markov chain, a piecewise-deterministic occupancy process, or a piecewise ODE on each node coupled by jump-shedding. The graph, not the local vector field, carries organotropism [4,7,9].

### Observation maps (lumped outputs)

Write \(\Phi\) for the map from graph state to what a local ODE typically sees.

| Map | Formula (schematic) | What it erases |
| --- | --- | --- |
| Primary only | \(y=x_{\mathrm{primary}}\) or \(y=T\) | All downstream occupancy |
| Summed burden | \(y=\sum_{i\in V} x_i\) | Which nodes contribute |
| Detectable sum | \(y=\sum_i \mathbf{1}_{x_i\ge \tau} x_i\) | Occult occupancy below \(\tau\) [12,13] |
| Count of lesions | \(y=\#\{i:x_i\ge\tau\}\) | Identity of \(i\), routes, times |
| First-event time | \(y=\inf\{t:\max_{i\neq\mathrm{primary}}x_i\ge\tau\}\) | Which site fired, later path |
| DMFS curve | population survival of first-event times | Site, route, growth vs dissemination split [42] |
| Autopsy histogram | empirical \(\pi_i\) at death | Times, order, transients [25–27] |

Adequacy criterion (research-scoped). A Class A model with output \(\Phi\) is adequate for a question \(Q\) if and only if every pair of Class B trajectories with the same \(\Phi\)-path give the same answer to \(Q\). If \(Q\) asks for a seeded set, a first site, a route, a waiting time, a spreader/sponge role, or a secondary-seeding fraction, Class A is not adequate.

### Graph observables that remain unidentified under lumped outputs

The following remain unidentified, as symbols, under the maps in the table. “Unidentified” here means: not uniquely determined by \(\Phi\), even in the noise-free structural sense, unless extra structure (anatomical sparsity, a time proxy, site-resolved data, phylogeny) is added and declared [32,36–42].

1. **Occupancy vector \(\sigma\) and seeded set \(S=\{i:\sigma_i=1\}\).** Any permutation of mass among nodes with the same sum is invisible to \(y=\sum x_i\).

2. **First-site identity.** Distinct first nodes can share a first-event time. Newton’s breast-cancer analysis treated first site as a state that structures the rest of the walk [28]; a DMFS time discards that state [42].

3. **Transition matrix \(P\) and edge rates.** A dense \(P\) has \(O(n^2)\) entries; an autopsy histogram supplies \(O(n)\) frequencies. Newton’s steady-state step was a closure of that gap, not a measurement of transients [26,27,32]. Gerlee and Johansson reduced the gap by anatomical sparsity and stage-as-time; they still report relative rates, not calendar rates, and they still cannot read skip-forbidden edges from incidence tables alone [32].

4. **Spreader versus sponge roles.** These are functions of in- and out-flow on \(P\) or of downstream occupancy given a first site [27,28]. They are undefined on a scalar \(T(t)\).

5. **Transit times and waiting-time laws.** Event-time outputs retain a clock and lose the edge that rang it. Stage as a time proxy yields relative \(\lambda,\varphi\), not days [32].

6. **Organ-specific colonization / carrying capacities / soil parameters.** Seed-and-soil and organotropism reviews name node-specific survival after arrival [3,4,7,9]. A summed burden does not allocate failure between “never arrived” and “arrived and died”. Filter-flow further mixes filtration with soil [31].

7. **Direct versus secondary seeding (\(\lambda\) versus \(\varphi\)).** Apparent primary-to-distant efficiency is inflated if occult intermediates shed onward [30–32]. A local ODE with one dissemination parameter cannot split the two without a latent occupancy layer, at which point it has become Class B.

8. **Self-seeding flux.** Primary volume can rise because local growth rose, or because a return edge is active, or because secondary deposits feed that edge [30,33–35]. Scott and colleagues showed the third path is required for self-seeding to matter as a growth driver [30]. The extra local growth term is therefore unidentified as a mechanism from \(T(t)\) alone.

9. **Colony-size distribution versus total metastatic burden.** Baratchart and colleagues: total burden describable, size distribution not, until merging is added [21]. Iwata’s \(u(x,t)\) is already a finer output than \(T(t)\) and is still not an organ graph [18].

10. **Occult micrometastatic occupancy.** By construction invisible to maps with threshold \(\tau\) [12,13]. Naming it a hidden local parameter, rather than an unobserved node state, is the smuggling step thesis 04 flags in a different (hybrid-switching) language; this thesis flags it as missing graph occupancy.

11. **Historical path / phylogeny.** Which edges were actually used. Gundem and colleagues reconstructed branching and reseeding in lethal metastatic prostate cancer [44]. Naxerova and Jain reviewed tumour phylogenetics as the tool for that reconstruction [43]. Lumped burden is silent.

### What would identify them (methods, not a claim that this repository did so)

Site-resolved longitudinal occupancy, first-site labels, anatomical edge lists, stage or another time proxy, colony-size imaging, and phylogenetic paths are the measurement classes that move items 1–11 toward identifiability in the cited papers [21,28,32,42–44]. Adding those measurements changes the observation map. It does not license a clinical product [50]. This repository does not analyse those data.

### Refusal of clinical metastasis-treatment claims

The following promotions are forbidden in this manuscript and in repository metadata.

1. Do not treat a Markov diagram as a targeting list. Spreader/sponge is a fitted network role [27,28], not an indication for resection, irradiation, or drug delivery.
2. Do not treat oligometastasis as a consequence of this thesis. Newton’s discussion of possible consequences in the oligometastatic setting [28] remains a citation, not a care recommendation.
3. Do not treat filter-flow anatomy as personalized therapy [31]. The capillary-bed constraint is kept; the therapy clause is refused.
4. Do not treat Chen’s claims-network prediction, Newton’s first-site prediction, or Gerlee’s stage-conditional occupancy probabilities as a CDS engine [24,28,32].
5. Do not treat GLOBOCAN counts, WHO fact-sheet language, or cascade reviews as parameters [1,2,5–11].
6. Do not write OnCo knowledge, NSTG text, or a Disease Profile board into \(P\), \(\lambda\), \(\varphi\), or a soil coefficient [47–49].
7. Do not edit `CancerODE` in the name of metastasis [46,47].
8. Do not invent DOIs, trial results, or identified Θ.

Gate 0 is this list. A sentence that predicts a site in a published research cohort remains a citation. A sentence that recommends an action on a patient is out of scope.

### Relation to theses 01–03 (and to 04 as a neighbour)

| Thesis | Question | Object this thesis does not reuse as its problem |
| --- | --- | --- |
| 01 | How to bind an oncology knowledge graph to a frozen ODE without skip-level promotion into Θ | OnCo adapter, LDHA/`p_lactate` [47] |
| 02 | How to explore in-silico pathology under NSTG as a qualitative constraint | CaseCard, NSTG-as-coefficient [48] |
| 03 | How to export a versioned Disease Profile research object | Profile schema, thinking-lab board [49] |
| 04 (neighbour) | Occult residual disease as hybrid switching, not a hidden continuous parameter | Filippov modes; cited only to avoid double-counting occult-as-Θ |
| **05** | Local burden ODE versus organ-graph spreading under lumped outputs | Anatomical network identifiability |

The conversion ladder of thesis 01 still applies [47]:

```
Knowledge
  --cite--> Evidence
    --interpret--> Hypothesis
      --propose--> Mechanism
        --identify--> Parameter
          --simulate--> Prediction
            --test--> Experiment
              --write--> Evidence
```

An anatomical graph is a candidate mechanism-plus-state, not a parameter dump. Autopsy frequencies are evidence of a histogram, not of a unique \(P\) without a declared closure [25–27,32]. A filter-flow cartoon is knowledge of anatomy, not an identified \(\lambda\) [31].

---

## Analysis

The analysis is a reading of published identifiability and network results against the observation maps above. It is not a new fit.

### Local ODEs are adequate only for lumped-invariant questions

If \(Q\) is “does this growth-law family describe a volume series as well as another family?”, Class A is the right object and remains contested even there [15,16]. If \(Q\) is “does total metastatic burden after xenograft injection follow a shedding-and-growth law?”, Class A or Iwata-type transport can be adequate for the sum and still fail the size distribution [20,21]. If \(Q\) is “which organ is seeded first, and does that node behave as a spreader?”, \(\Phi\) must retain site identity [27,28]. A local ODE with output \(T(t)\) cannot answer \(Q\) because every occupancy path with the same sum is an indistinguishable pre-image.

CONFLUENCE’s 15-dimensional local state does not change the test. Fifteen local coordinates are not \(n\) organ nodes. Enlarging \(d\) without changing \(\Phi\) does not identify \(P\) [46,47].

### Underdetermination is already on the record

Newton and colleagues constructed \(P\) from an autopsy histogram by assuming that the observed site frequencies are a stationary distribution of the walk [26,27]. Gerlee and Johansson call that step a response to underdetermination [32]. The implication for Class A is immediate: if even an organ-resolved *histogram* does not identify \(P\) without a closure, a scalar burden — which is a further lumping of that histogram — does not identify \(P\) either.

Adding anatomical sparsity and a time proxy, as Gerlee and Johansson did, identifies a smaller set of *relative* edge rates on two specific graphs (tongue lymphatic stations; a coarse ovarian map) [32]. That is a change of observation map and of model class, not a rehabilitation of a local ODE. The rates remain relative because stage is not clock time. Skip-metastases, if real rather than occult intermediates, would reopen edges that the model forbade [32]. Those caveats stay attached.

### Filter-flow makes lumping actively misleading

Under filter-flow, a cell leaving a visceral primary does not sample organs independently [29,31]. Lung is a first capillary bed for venous-side shedding; apparent liver or bone colonization from that primary may be secondary [31,32]. A one-parameter dissemination term in \(\dot T\) attributes to “metastatic potential” a mixture of filtration, occult intermediate occupancy, and soil. Scott and colleagues showed that self-seeding as a driver of primary growth is negligible without those intermediates [30]. Therefore a local extra growth term labelled self-seeding is unidentified as a mechanism from primary volume.

### Survival curves do not rescue the graph

Álvarez-Arenas and colleagues studied a two-parameter mechanistic model of time to distant metastatic relapse, with population distributions on growth \(\alpha\) and dissemination \(\mu\) [42]. Practical identifiability of that pair from a DMFS curve required the percentage of patients with metastasis at diagnosis. Covariates could be assigned to \(\alpha\) or \(\mu\) only after that closure. The output is already a lumped event time. The state is not an organ graph. The result is a warning, not a licence: if two scalars need an extra summary statistic, \(O(n)+O(|E|)\) graph coordinates will not appear from the same curve.

### Size distributions and phylogenies are still not organ graphs — and still exceed lumped ODEs

Iwata’s size coordinate and Baratchart’s MRI distribution ask how large colonies are, not which organs they occupy [18,21]. Gundem’s phylogenetic trees ask which clones reached which sites and whether reseeding occurred [44]. Both measurement classes split pre-images that a summed burden glues together. Neither is supplied by a local ODE. Naxerova and Jain’s review is cited for that methodological point, not as a CONFLUENCE pipeline [43].

### Worked contrast (hypothetical, not a fitted patient)

Consider two occupancy paths on a three-node graph \(\{\mathrm{primary},\mathrm{lung},\mathrm{liver}\}\) with the same summed detectable burden after a fixed time: (i) primary plus lung sponge, no liver; (ii) primary plus liver, lung negative. A Class A model with \(y=\sum x_i\) cannot distinguish them. Class B questions — first site, subsequent arterial risk, spreader role of lung — differ. If a laboratory reports a “metastasis parameter” from \(y\), it has named a mixture, not a mechanism. This diagram is illustrative. It is not a cohort result.

---

## Discussion

The anatomical-graph literature does not abolish local growth laws. It changes the question those laws are allowed to answer. Volume series remain the right objects for comparing Gompertz against logistic in a xenograft [15,16]. They are the wrong objects for claiming that organotropism, first-site identity, or secondary seeding has been identified.

The honest remainder is large. Autopsy histograms are end-of-life, not trajectories, and Newton’s series is untreated and historically dated [25–27]. Claims networks mix coding practice with biology [24]. Stage is a crude clock [32]. Filter-flow abstracts capillary beds as filters and does not identify soil coefficients [31]. Binary occupancy ignores colony size; Iwata-type size distributions ignore organ identity [18,32]. Phylogenies are still rare relative to imaging [43,44]. Practical identifiability of even two scalars from DMFS is fragile [42]. Those limits are reasons to keep symbols unidentified, not reasons to collapse back to a local ODE and speak as if the graph had been seen.

This thesis does not compete with theses 01–03. Those documents fence knowledge-to-parameter promotion, guideline-to-coefficient promotion, and chart-to-profile promotion [47–49]. This document fences lumped-burden-to-anatomical-graph promotion. A laboratory can obey all four fences at once: refuse OnCo as \(\Theta\), refuse NSTG as a rate, refuse a profile as CDS, and refuse a summed volume as a transition matrix.

Future in-silico work, if done, should change the observation map first: site-resolved occupancy, waiting times, anatomical edge lists declared as knowledge rather than as data, and phylogenetic labels where they exist. Any such work stays behind Gates 0–5 until an identification step is actually performed and reported with uncertainty. Gate 8 remains unclaimed.

---

## Limitations

1. No new parameter estimate, no new figure from data, no software experiment in this repository.
2. The adequacy criterion is logical (invariance under lumped-equivalent trajectories), not a numerical profile-likelihood for a named \(P\).
3. Literature models disagree on state (walker versus binary occupancy versus size density versus spatial grid). The unidentified list is the union of what lumped maps hide in each; it is not a claim that one representation is true.
4. CONFLUENCE, OnCo, NSTG, and Disease Profiles are neighbouring artefacts. They are not materials of a graph fit.
5. Clinical datasets cited from other groups (SEER ovarian, Memorial Sloan Kettering breast, untreated autopsy, Medicare claims, UROCCR DMFS) are not re-analysed here and are not a validation of this thesis as a product [24,25,28,32,42].

---

## Conclusion

A local tumour-burden ODE remains adequate only for questions that do not change when the anatomical path behind a lumped output is swapped. Once dissemination is written as stochastic spreading on an organ-to-organ graph, the occupancy vector, first-site identity, transition rates, spreader–sponge roles, transit times, organ-specific colonization, secondary-seeding fluxes, self-seeding, occult occupancy, and historical path stay unidentified under primary volumes, summed burdens, lesion counts, and DMFS curves [21,26–28,30–32,42–44]. That is an identifiability statement. It is not a treatment of metastasis [50].

---

## Acknowledgements

Correspondence: kelechiogbonna300@gmail.com. Institutional email: pending. No document DOI is registered.

---

## References

Numbered Vancouver list: see [`refs/references.md`](refs/references.md). Journal DOIs in that list were checked against Crossref or publisher records on 21 September 2026. No DOI is invented. This document has no registered DOI.
