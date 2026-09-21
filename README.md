# Metastasis as Stochastic Spreading on Organ-to-Organ Anatomical Graphs

**Thesis #5** — computational research thesis, formatted to match B.Sc. project chapter structure (Nile University style) for journal/thesis handoff.

**Author:** Kelechi Emeka Ogbonna
**Email:** kelechiogbonna300@gmail.com
**Affiliation:** Independent computational research / Project Confluence
**Date:** 21 September 2026

This manuscript uses the same chapter skeleton as Kelechi Emeka Ogbonna’s 2022 Nile University B.Sc. project (*Carica papaya* AgNP antidiabetic). **It is not that wet-lab study.** Results here are in-silico identifiability numbers on a toy five-node anatomical graph. They are not patient outcomes.

## Non-claims

This thesis is **research only**. It is not a medical device, not clinical
decision support, not a protocol, not a dose, and not a cure. It does not
claim that targeting spreader organs, oligometastatic lesions, or
filter-flow routes treats metastasis. No DOI is registered for this
document; do not invent one.

See [DISCLAIMER.md](DISCLAIMER.md).

```text
Knowledge ≠ Evidence ≠ Mechanism ≠ Parameter ≠ Prediction
```

A local tumour-burden ODE is not an anatomical graph. A lumped output is
not an identified transition matrix.

## The problem (one sentence)

Does a local tumour-burden ordinary differential equation remain an adequate in-silico object once dissemination is posed as a stochastic process on an organ-to-organ anatomical graph, or do graph observables remain unidentified under current lumped outputs?

That sentence is the whole job. Chapter Four is the toy graph that makes the sentence fail closed.

## How this is not theses 01–04

| Thesis | Object already claimed | What #5 is not repeating |
| --- | --- | --- |
| **01** | Evidence-gated OnCo adapter around a frozen cancer-state ODE | Not another knowledge-graph bind |
| **02** | NSTG-constrained YAML `CaseCard` → `PathwaySketch` | Not another card |
| **03** | Disease Profile as a versioned research object | Not another schema |
| **04** | Hybrid / Filippov occult modes | Not another switching specification |
| **05** | Organ-to-organ graph versus lumped local burden | Anatomical-network identifiability |

Hub index: [research-theses-hub](https://github.com/cloudynirvana/research-theses-hub)
(`NEXT_PAPERS.md` item NP-05).

## Files

| Path | Role |
| --- | --- |
| `THESIS.md` | Full manuscript in Nile University B.Sc. chapter structure (Vancouver citations) |
| `THESIS.pdf` | Citeable PDF built from the Markdown |
| `refs/references.md` | Numbered Vancouver bibliography (verified journal DOIs only) |
| `CITATION.cff` | Citation metadata (no document DOI) |
| `DISCLAIMER.md` | Research-only disclaimer |
| `scripts/identifiability_experiment.py` | Chapter Four laboratory (seed 5) |
| `results/identifiability_results.json` | Machine-readable Chapter Four numbers |
| `scripts/build_pdf.sh` | Rebuild `THESIS.pdf` (`bash scripts/build_pdf.sh`) |

## Chapter skeleton

Title page · Declaration · Abstract · Table of Contents · **CHAPTER ONE — INTRODUCTION** (1.1 Background; 1.2 STATEMENT OF RESEARCH PROBLEM; 1.3 JUSTIFICATION OF STUDY; 1.4 AIM AND OBJECTIVES; 1.5 SIGNIFICANCE; 1.6 SCOPE) · **CHAPTER TWO — LITERATURE REVIEW** · **CHAPTER THREE — MATERIALS AND METHODS** (computational) · **CHAPTER FOUR — RESULTS** (in-silico identifiability) · **CHAPTER FIVE — DISCUSSION, CONCLUSION AND RECOMMENDATION** · REFERENCES.

## How to cite

Ogbonna KE. Metastasis as stochastic spreading on organ-to-organ anatomical graphs: adequacy of local tumour-burden ODEs under lumped outputs [Internet]. Thesis #5 computational research thesis. 21 September 2026 [cited YYYY Mon DD]. Available from: https://github.com/cloudynirvana/thesis-05-metastasis-anatomical-graphs

Prefer `CITATION.cff` for machine-readable citation. When a document DOI is later minted, add it there only after it exists.

## Licence

Manuscript text in this repository is provided for scholarly reuse with
attribution (MIT). Cited papers remain under their publishers’ licences.
Computational research only. Not a care product.
