---
title: "Predicting non-coding variant effects with AlphaGenome"
collection: publications
permalink: /publication/2026-04-08-alphagenome_cell_research_highlight
excerpt: 'Research highlight covering AlphaGenome, a sequence-to-function model that uses up to a megabase of genomic context at base-pair resolution to predict regulatory activity and single-nucleotide variant effects. We discuss design trade-offs (breadth vs. specialization, scale vs. resolution), benchmarking and ablations, and open challenges including combinatorial variation, distal cis-regulatory validation, and cellular context.'
date: 2026-04-08
venue: 'Cell Research (Research Highlight)'
paperurl: 'https://www.nature.com/articles/s41422-026-01249-1'
citation: '<b>Murphy, A.E.*</b>, Nagai, M.* & Koo, P.K. <i>Cell Res.</i> (2026). https://doi.org/10.1038/s41422-026-01249-1'
---

Most trait- and disease-associated genetic variation lies in non-coding DNA and acts by altering gene regulation. Computational sequence-to-function models offer a scalable way to prioritise variants and reason about mechanism, but they face persistent tensions between integrating many molecular readouts versus specialising on one assay, and between modelling long-range *cis*-regulatory context versus resolving predictions at single-base resolution.

This *Cell Research* research highlight summarises recent work on **AlphaGenome**, which addresses these tensions through architectural choices such as sequence sharding, transformer layers for distal interactions, expanded outputs (including contact maps and splicing-related tasks), and ensemble distillation for accuracy without the full cost of ensembling at inference. We outline how the model was benchmarked on single-nucleotide variant effects across diverse assays, what ablations suggest about resolution and training context, and where important limitations remain — including complex alleles, personal-genome-style combinatorial effects, rigorous evaluation against distal perturbation data, and dependence on cellular context implicit in the training data.

[Read the highlight at Cell Research](https://www.nature.com/articles/s41422-026-01249-1)

Recommended citation: <b>Murphy, A.E.</b>, Nagai, M. & Koo, P.K. <i>Cell Res.</i> (2026). https://doi.org/10.1038/s41422-026-01249-1