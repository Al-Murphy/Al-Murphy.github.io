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
<p>Hi, I'm Alan Murphy, a computational biologist conducting my postdoctoral research in <a href="https://koolab.cshl.edu/">Dr. Peter Koo's lab</a> at Cold Spring Harbor Laboratory. I build <strong>sequence-to-function (seq2func) models</strong> of gene regulation — models that map DNA sequence to measured regulatory activity — and I work on making them <strong>reliable where they are currently weakest</strong>: on genetic variants, on designed regulatory elements, and in the cell types where disease acts.</p>

<p>Most variants associated with common disease fall outside protein-coding sequence, where their effect on gene regulation is usually unknown, and the same sequence behaves differently from one cell type to the next. Models that read <strong>both the sequence and the cell</strong> offer a route to interpreting those variants and to designing regulatory elements active in a single cell type — but only if their predictions hold outside the data they were trained on. Establishing where they do, extending them where they do not, and using them to design elements for the cell types where disease acts is the programme I will build my laboratory around.</p>

<p>Beyond research, I co-created and serve as editor for the <a href="https://genomicsxai.github.io/">Genomics × AI</a> blog, a growing community hub highlighting methods and applications at the intersection of genomics and machine learning. This initiative reflects my dedication to <strong>scholarly leadership and knowledge sharing</strong> in computational biology.</p>
</div>

&nbsp;

## Research Programme

<div style="text-align: justify">
<p>Two obstacles stand between a disease locus and a mechanism: <strong>which variant is causal</strong>, and <strong>which cell type it acts in</strong>. Seq2func models could resolve both — a variant's effect is the difference between scoring its two alleles, and a promising regulatory element is one the model scores highly in the target cell type — yet they are least reliable in exactly these settings. Two causes account for that, and my laboratory will be organised around measuring and correcting each: the <strong>sequence</strong>, because a rare variant or a designed element is unlike anything in the training data, and the <strong>cell</strong>, because an element is only active where the regulators that drive it are present.</p>
</div>

<div class="aim-grid">
  <div class="aim-card">
    <span class="aim-card__label">Aim 1</span>
    <h3 class="aim-card__title">Establish where regulatory models can be trusted</h3>
    <p class="aim-card__body">Accuracy is reported as a single number over held-out regions of the genome, which says little about a variant in the cell type where a disease acts. I will measure how accuracy falls across classes of sequence and as cellular context moves away from a model's training data. The result is a public resource reporting the accuracy to expect for a given model, sequence and cell type.</p>
  </div>
  <div class="aim-card">
    <span class="aim-card__label">Aim 2</span>
    <h3 class="aim-card__title">Correct models with perturbation data</h3>
    <p class="aim-card__body">Genome-wide profiling shows which sequence features accompany regulatory activity; perturbation experiments show what changing one of them actually does. My laboratory will refine models on the full body of published reporter and CRISPR interference screens, and establish whether a correction learned in one cell type transfers to the cell types where disease acts.</p>
  </div>
  <div class="aim-card">
    <span class="aim-card__label">Aim 3</span>
    <h3 class="aim-card__title">Design regulatory elements selective for a chosen cell type</h3>
    <p class="aim-card__body">Gene therapies can restrict a transgene to one cell type through the regulatory element placed in front of it, but candidates must be narrowed down long before anything is synthesised. I will build models that score candidate elements across hundreds of cell types, so an element can be designed for one and screened against all the others, then validated experimentally.</p>
  </div>
</div>

<div style="text-align: justify">
<p>Throughout, the models, datasets and evaluation protocols behind this work are <strong>released openly</strong>. The longer goal is a model that can be trusted on a variant nobody has assayed, in a cellular state nobody has screened.</p>
</div>

&nbsp;

<p class="home-button-row">
  <a class="btn" href="/cv/" target="_blank" rel="noopener">CV</a>
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
    {% for post in site.publications reversed %}
      {% include archive-single-cv.html %}
    {% endfor %}
  </ul>
</div>