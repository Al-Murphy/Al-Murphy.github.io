---
permalink: /
title: "Alan Murphy"
excerpt: "About me"
author_profile: true
sidebar_right: true
redirect_from: 
  - /about/
  - /about.html
---
<font size="3">Computational Biologist | Postdoctoral Researcher, Cold Spring Harbor Laboratory, New York</font>

&nbsp;
&nbsp;

<div style="text-align: justify">
Hi, I'm Alan Murphy, a computational biologist conducting my postdoctoral research in <a href="https://koolab.cshl.edu/">Dr. Peter Koo's lab</a> at Cold Spring Harbor Laboratory. I build <strong>sequence-to-function (seq2func) models</strong> of gene regulation — models that map DNA sequence to molecular and cellular activity — and I focus on making them <strong>reliable when it matters</strong>: when sequences are perturbed, when regulatory organisation is rearranged, or when the cellular context changes. My goal is to turn seq2func models from accurate pattern matchers into <strong>trustworthy, mechanistically informative platforms</strong> for interpreting non-coding variants, designing perturbation experiments, and engineering synthetic regulatory sequences.

Beyond research, I co-created and serve as editor for the <a href="https://genomicsxai.github.io/">Genomics × AI</a> blog, a growing community hub highlighting methods and applications at the intersection of genomics and machine learning. This initiative reflects my dedication to <strong>scholarly leadership and knowledge sharing</strong> in computational biology.

</div>

&nbsp;

## Research Vision

My research programme aims to build seq2func models that reveal how regulatory <strong>sequence, genomic context, and cellular state</strong> combine to determine context-specific gene expression — and that <strong>remain reliable under the conditions where they are actually used</strong>. State-of-the-art models achieve strong predictive performance on held-out genomic regions, but that alone does not establish that they have learned regulatory logic which stays valid when sequences are perturbed or when regulatory organisation is rearranged.

I frame model failures through the lens of <strong>distribution shift</strong>:

- <strong>Covariate shift</strong> — sequences or perturbations that are poorly represented in the training data.  
- <strong>Concept shift</strong> — the same sequence behaving differently because the cellular context has changed.

I diagnose these failures systematically and close them by learning from <strong>targeted perturbation experiments</strong> — discarding genome-wide knowledge where it misleads, and keeping predictions reliable even when perturbations shift the cell state itself.

How reliably models handle these shifts ultimately determines their usefulness across the applications that depend on them:

- <strong>Interpreting non-coding variants</strong> — predicting the functional consequences of regulatory genetic variation.  
- <strong>Designing perturbation experiments</strong> that reveal cis-regulatory biology.  
- <strong>Engineering synthetic regulatory sequences</strong> with tunable properties.

Throughout, I develop <strong>open-access tools and resources</strong> to promote reproducibility and empower the genomics community.

&nbsp;

<p class="home-button-row">
  <a class="btn" href="/cv/" target="_blank" rel="noopener">Download CV</a>
  <a class="btn" href="https://scholar.google.com/citations?user=oH1tIr0AAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>
  <a class="btn" href="https://genomicsxai.github.io/" target="_blank" rel="noopener">Genomics × AI Blog</a>
</p>

&nbsp;

## News
<ul class="news-list">
  {% for item in site.data.news %}
    <li class="news-item">
      <span class="news-date">{{ item.date }}</span>
      <span class="news-body">{{ item.body | markdownify }}</span>
    </li>
  {% endfor %}
</ul>

## Selected Publications
<p class="publications-note">
  This is a selection of recent work. For a complete and always up-to-date list, see my
  <a href="https://scholar.google.com/citations?user=oH1tIr0AAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar profile</a>.
</p>
<div class="publications-scroll">
  <ul>
    {% for post in site.publications %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>
</div>