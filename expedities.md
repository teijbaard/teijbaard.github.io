---
layout: default
title: "Expedities"
description: "Alle avonturen van Tijmen op Stoom — van stoomtreinen op de Veluwe tot ICE-spotting in Duitsland."
permalink: /expedities/
---

<style>
  .expedities-hero {
    background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy-mid) 100%);
    color: var(--white);
    padding: 4rem 0;
    text-align: center;
  }
  .expedities-hero h1 {
    font-size: clamp(3rem, 8vw, 6rem);
    color: var(--white);
    margin-bottom: 0.5rem;
  }
  .expedities-hero h1 span { color: var(--ochre); }
  .expedities-hero p { color: rgba(255,255,255,0.7); max-width: 500px; margin: 0 auto; font-size: 1.05rem; }

  .expedities-list {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 4rem 1.25rem;
  }

  .expedities-count {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.1rem;
    color: var(--text-muted);
    letter-spacing: 0.1em;
    margin-bottom: 2rem;
  }
  .expedities-count span { color: var(--ochre); }

  .expedition-list-item {
    display: grid;
    grid-template-columns: 80px 1fr auto;
    gap: 1.5rem;
    align-items: center;
    background: var(--white);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow);
    padding: 1.5rem;
    margin-bottom: 1.25rem;
    transition: transform var(--transition), box-shadow var(--transition);
    text-decoration: none;
    color: inherit;
    border-left: 5px solid var(--ochre);
  }
  .expedition-list-item:hover {
    transform: translateX(4px);
    box-shadow: var(--shadow-lg);
  }

  .exp-number {
    font-family: 'Bebas Neue', cursive;
    font-size: 3rem;
    color: var(--ochre);
    line-height: 1;
    text-align: center;
  }

  .exp-info {}
  .exp-title {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.6rem;
    color: var(--navy-dark);
    margin-bottom: 0.25rem;
    line-height: 1.2;
  }
  .exp-meta {
    font-size: 0.85rem;
    color: var(--text-muted);
    font-weight: 600;
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
  }
  .exp-meta span { display: flex; align-items: center; gap: 0.25rem; }

  .exp-excerpt {
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-top: 0.5rem;
    line-height: 1.6;
  }

  .exp-arrow {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.5rem;
    color: var(--ochre);
    flex-shrink: 0;
  }

  .empty-state {
    text-align: center;
    padding: 4rem 1rem;
    color: var(--text-muted);
  }
  .empty-state .big { font-size: 4rem; display: block; margin-bottom: 1rem; }
  .empty-state h2 { font-size: 2rem; color: var(--navy-dark); margin-bottom: 0.5rem; }

  @media (max-width: 600px) {
    .expedition-list-item { grid-template-columns: 56px 1fr; }
    .exp-arrow { display: none; }
    .exp-number { font-size: 2.2rem; }
  }
</style>

<section class="expedities-hero">
  <div class="container">
    <h1>Mijn <span>Expedities</span></h1>
    <p>Elk avontuur, elke reis, elke stoomwolk — hier bijgehouden voor altijd.</p>
  </div>
</section>
<div class="track-line"></div>

<div class="expedities-list">

  {% if site.expedities.size > 0 %}
  <p class="expedities-count">
    <span>{{ site.expedities.size }}</span> expedities gevonden
  </p>

  {% assign sorted = site.expedities | sort: 'date' | reverse %}
  {% for expeditie in sorted %}
  <a href="{{ expeditie.url | relative_url }}" class="expedition-list-item">
    <div class="exp-number">{{ expeditie.nummer | default: forloop.index }}</div>
    <div class="exp-info">
      <div class="exp-title">{{ expeditie.title }}</div>
      <div class="exp-meta">
        <span>📅 {{ expeditie.date | date: "%-d %B %Y" }}</span>
        {% if expeditie.locatie %}<span>📍 {{ expeditie.locatie }}</span>{% endif %}
        {% if expeditie.tags %}<span>🏷️ {{ expeditie.tags | join: ', ' }}</span>{% endif %}
      </div>
      {% if expeditie.excerpt %}
      <p class="exp-excerpt">{{ expeditie.excerpt | strip_html | truncate: 120 }}</p>
      {% endif %}
    </div>
    <div class="exp-arrow">→</div>
  </a>
  {% endfor %}

  {% else %}
  <div class="empty-state">
    <span class="big">🚂</span>
    <h2>Binnenkort hier!</h2>
    <p>De eerste expeditie-verslagen zijn onderweg. Abonneer op YouTube om niets te missen!</p>
    <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-primary mt-md">
      ▶ Volg op YouTube
    </a>
  </div>
  {% endif %}

</div>
