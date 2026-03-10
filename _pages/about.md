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
Hi, I'm Alan Murphy, a computational biologist conducting my postdoctoral research in <a href="https://koolab.cshl.edu/">Dr. Peter Koo's lab</a> at Cold Spring Harbor Laboratory. My research focuses on developing and refining <strong>sequence-to-function (seq2func) models</strong> that uncover the <strong>cis-regulatory code</strong> — the rules by which DNA sequence dictates gene regulatory activity — and that are interpretable, generalisable across contexts, and tightly coupled to experimental perturbations and functional readouts.

Beyond research, I co-created and serve as editor for the <a href="https://genomicsxai.github.io/">Genomics × AI</a> blog, a growing community hub highlighting methods and applications at the intersection of genomics and machine learning. This initiative reflects my dedication to <strong>scholarly leadership and knowledge sharing</strong> in computational biology.

</div>

&nbsp;

## Research Vision & Impact

I aim to uncover the <strong>cis-regulatory code</strong> — the rules by which DNA sequence dictates gene regulation — by developing <strong>interpretable, generalisable sequence-to-function (seq2func) models</strong>. My work integrates <strong>computational modeling and experimental perturbations</strong>, including functional assays, to systematically probe how regulatory sequences control cellular phenotypes.

Key goals of my research include:

- Building models that <strong>generalise across cell types and experimental contexts</strong>, enabling predictive insights beyond the training data.  
- Improving <strong>interpretability</strong>, so that computational predictions reveal mechanistic principles of gene regulation.  
- Developing <strong>open-access tools and resources</strong> to promote reproducibility and empower the genomics community.

Through this approach, I seek to <strong>bridge predictive modeling with mechanistic understanding</strong>, advancing both fundamental insights into gene regulation and the methodological foundations of regulatory genomics.

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