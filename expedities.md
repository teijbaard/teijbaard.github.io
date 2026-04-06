---
layout: default
title: "Expedities"
description: "Alle avonturen van Tijmen op Stoom — van stoomtreinen op de Veluwe tot ICE-spotting in Duitsland."
permalink: /expedities/
---

<style>
  .exp-list-hero {
    background: var(--surface);
    padding: 4.5rem 0;
    border-bottom: 1px solid var(--border);
  }
  .exp-list-hero h1 {
    font-size: clamp(2.75rem, 5vw, 4.5rem);
    color: var(--text);
    margin-bottom: 0.75rem;
    line-height: 1.05;
  }
  .exp-list-hero h1 em { font-style: normal; color: var(--rust); }
  .exp-list-hero p { color: var(--text-muted); max-width: 420px; }

  .exp-list-body {
    max-width: 720px;
    margin: 0 auto;
    padding: 4rem 1.5rem 5rem;
  }

  .exp-count {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    margin-bottom: 2rem;
  }
  .exp-count span { color: var(--rust); }

  .exp-list-item {
    display: grid;
    grid-template-columns: 64px 1fr 28px;
    gap: 1.25rem;
    align-items: center;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.375rem 1.5rem;
    margin-bottom: 0.875rem;
    text-decoration: none;
    color: inherit;
    transition: border-color var(--t), transform var(--t), box-shadow var(--t);
  }
  .exp-list-item:hover {
    border-color: var(--rust-mid);
    transform: translateX(3px);
    box-shadow: 0 4px 20px rgba(28,26,23,0.06);
  }

  .exp-list-num {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 2rem;
    color: var(--rust-mid);
    line-height: 1;
    text-align: center;
  }

  .exp-list-info {}
  .exp-list-title {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 1.1rem;
    color: var(--text);
    margin-bottom: 0.25rem;
    line-height: 1.25;
  }
  .exp-list-meta {
    font-size: 0.8rem;
    color: var(--text-muted);
    display: flex;
    gap: 0.875rem;
    flex-wrap: wrap;
    font-weight: 500;
  }
  .exp-list-excerpt {
    font-size: 0.875rem;
    color: var(--text-subtle);
    margin-top: 0.3rem;
    line-height: 1.6;
  }

  .exp-list-arrow {
    color: var(--border);
    font-size: 1.125rem;
    transition: color var(--t);
  }
  .exp-list-item:hover .exp-list-arrow { color: var(--rust); }

  .empty-state {
    text-align: center;
    padding: 5rem 1rem;
  }
  .empty-state .icon { font-size: 3.5rem; display: block; margin-bottom: 1rem; }
  .empty-state h2 { font-size: 2rem; color: var(--text); margin-bottom: 0.5rem; }
  .empty-state p { color: var(--text-muted); margin-bottom: 1.5rem; }

  @media (max-width: 480px) {
    .exp-list-item { grid-template-columns: 44px 1fr; }
    .exp-list-arrow { display: none; }
    .exp-list-num { font-size: 1.6rem; }
  }
</style>

<section class="exp-list-hero">
  <div class="container">
    <span class="label">Mijn avonturen</span>
    <h1>Alle <em>expedities</em></h1>
    <p>Elk avontuur, elke reis, elke stoomwolk — hier bijgehouden voor altijd.</p>
  </div>
</section>

<div class="container">
  <div class="exp-list-body">

    {% if site.expedities.size > 0 %}
    <p class="exp-count"><span>{{ site.expedities.size }}</span> expedities</p>

    {% assign sorted = site.expedities | sort: 'date' | reverse %}
    {% for exp in sorted %}
    <a href="{{ exp.url | relative_url }}" class="exp-list-item">
      <div class="exp-list-num">{{ exp.nummer | default: forloop.index }}</div>
      <div class="exp-list-info">
        <div class="exp-list-title">{{ exp.title }}</div>
        <div class="exp-list-meta">
          <span>{{ exp.date | date: "%-d %B %Y" }}</span>
          {% if exp.locatie %}<span>{{ exp.locatie }}</span>{% endif %}
        </div>
        {% if exp.excerpt %}
        <div class="exp-list-excerpt">{{ exp.excerpt | strip_html | truncate: 110 }}</div>
        {% endif %}
      </div>
      <span class="exp-list-arrow">→</span>
    </a>
    {% endfor %}

    {% else %}
    <div class="empty-state">
      <span class="icon">🚂</span>
      <h2>Binnenkort hier!</h2>
      <p>De eerste expeditie-verslagen zijn onderweg.</p>
      <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-primary">▶ Volg op YouTube</a>
    </div>
    {% endif %}

  </div>
</div>
