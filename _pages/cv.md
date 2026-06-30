---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---
<hr>
{% include base_path %}

## Professional Summary
<hr>
<div style="text-align: justify"><font size="3">I am a computational biologist and postdoctoral researcher at Cold Spring Harbor Laboratory, working in Prof. Peter Koo's group. My research focuses on developing sequence-to-function models to uncover the <i>cis</i>-regulatory code, with an emphasis on interpretability, generalisation across biological contexts, and integration with experimental perturbations and functional readouts. I am particularly interested in bridging predictive modelling with mechanistic understanding, using machine learning to derive biologically meaningful representations of regulatory sequence function. More broadly, my work aims to advance principled approaches for modelling high-dimensional genomic data, with a focus on robustness, reproducibility, and cross-context inference.</font></div>

## Core Expertise
<hr>
* Sequence-to-function modelling for regulatory genomics
* Interpretable machine learning
* Genomic foundation & language models
* Active learning & lab-in-the-loop systems
* Continual learning for genomics
* Representation learning in biological systems
* Genetic variant effect prediction
* Gene expression modelling
* Epigenetic data modelling
* Single-cell genomic analysis
* Multi-modal genomic data integration

## Experience
<hr>
* <b>Postdoctoral Research Scientist</b> - Koo Lab, Cold Spring Harbor Laboratory (CSHL), New York <b>(2025–Present)</b><br>
	<div style="text-align: justify"><font size="3">Developing and analysing deep learning models to characterise the <i>cis</i>-regulatory code from genomic sequence. Designing approaches that integrate perturbation data (e.g. MPRA and functional assays) to improve causal inference and mechanistic interpretability of regulatory models, and adapting large-scale sequence models for variant and cis-regulatory element effect prediction, including applications in cancer cell lines. A central theme is model generalisation and robustness across datasets, with a focus on distribution shift and cross-context prediction.</font></div>

* <b>Ph.D. Researcher</b> - UK Dementia Research Institute, Imperial College London <b>(2021–2025)</b><br>
	<div style="text-align: justify"><font size="3">Worked with Dr. Nathan Skene to design <i>Enformer Celltyping</i>, a deep learning framework to predict cell type-specific regulatory effects of genetic variation, including extrapolation to previously unseen cell types. Developed deep learning models for regulatory genomics, including prediction of gene expression from epigenomic profiles, to study mechanisms in neurodegenerative disease. Developed computational and statistical methods for single-cell RNA-seq analysis, and authored <i>MungeSumstats</i>, a widely used Bioconductor package for the standardisation and quality control of GWAS summary statistics.</font></div>

* <b>Research Assistant</b> - Overton Group, Queen's University Belfast <b>(2020–2021)</b><br>
	<div style="text-align: justify"><font size="3">Co-developed a systems biology and machine learning framework to identify cell type- and state-specific gene interaction networks across biological contexts, implemented as the open-source tool COSNI.</font></div>

* <b>Data Analytics Consultant</b> - Pricewaterhouse Coopers (PwC), Dublin <b>(2017–2020)</b><br>
	<div style="text-align: justify"><font size="3">Led multiple data analytics projects across a wide variety of engagements, completing all aspects of analytics pipelines from investigation, ETL, cleansing, analysis, modelling, insight and the deployment of automated solutions. Tangible results included correcting over €30 million worth of loans in arrears in one of Ireland's largest banks and increasing the success rate of targeted enforcement in a public sector body by over 15%.</font></div>

* <b>Data Analyst</b> - Aon Centre for Innovation and Analytics (ACIA), Dublin <b>(2016–2017)</b><br>
	<div style="text-align: justify"><font size="3">Gained real-world experience in data analytics, decision making and applied statistics, and developed best-practice project management skills. Designed, developed and implemented an in-house skills matrix system for senior management, giving insights into employee utilisation and predicting possible future skill shortages.</font></div>

## Scientific Leadership
<hr>
* <b>Lead Editor</b> - <a href="https://genomicsxai.github.io/">Genomics × AI</a> <b>(2026–Present)</b><br>
	<div style="text-align: justify"><font size="3">Lead the strategic and editorial direction of a community-driven platform for rapid scientific communication at the intersection of genomics and machine learning. Coordinate between the Editorial Board and Steering Committee to define scope, maintain quality standards, and guide long-term development, and oversee a structured, GitHub-based review process for short-form articles, enabling rapid dissemination of ideas, tutorials, and incremental or negative results.</font></div>

Selected first-author articles:
* Murphy, A., Koo, P. [Benchmarking seq2func models on distal enhancer effects with CRISPRi screens](https://genomicsxai.github.io/blogs/2026-007/), Genomics × AI Blog (2026).
* Murphy, A., Koo, P. [Adapting AlphaGenome to MPRA data](https://genomicsxai.github.io/blogs/2026-002/), Genomics × AI Blog (2026).
* Murphy, A., Nagai, M., Buendia, A., Kundaje, A., Koo, P. [Fine-tuning AlphaGenome in native JAX/Haiku](https://genomicsxai.github.io/blogs/2026-003/), Genomics × AI Blog (2026).

## Education
<hr>
* Ph.D. in Computational Biology (Brain Sciences), Imperial College London, 2021–2025
* M.S. in Bioinformatics and Computational Genomics, Queen's University Belfast, 2020–2021
* B.S. in Management Science and Information Systems, Trinity College Dublin, 2013–2017

## Selected Publications
<hr>
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
## Teaching
<hr>
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Awards
<hr>
* Prize for outstanding TA, Quantitative Biology Program, Cold Spring Harbor Laboratory (2025)
* The [Genetics Society](https://genetics.org.uk/) Conference Early Career Researcher Grant (2023)
* Prize for Computational Reproducibility, UK Dementia Research Institute (2023)

## Presentations
<hr>
* Causal refinement for genomic deep learning models through continual learning, MLCB, US (2025)
* Predicting cell type-specific epigenomic profiles accounting for distal genetic effects, Kipoi Summit, Germany (2023)
* Single-cell genomics for Alzheimer's disease, ADDI Learning Series, UK (2023)

## Academic Service
<hr>
* <b>Mentorship:</b> Supervised 1 PhD, 4 MSc, 4 undergraduate, and 1 high school research student.
* <b>Peer Review:</b> Nature (1), Nature Methods (3), Nature Genetics (3), Nature Communications (1), Genome Research (2), Science (1), Machine Learning in Computational Biology (MLCB), Intelligent Systems for Molecular Biology (ISMB).
