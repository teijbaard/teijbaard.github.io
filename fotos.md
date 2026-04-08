---
layout: default
title: "Foto's"
description: "Alle foto's van Tijmen op Stoom — gefilterd op vervoerder, treinstel of evenement."
permalink: /fotos/
---

<style>
  /* ============================================================
     FOTOS PAGE
     ============================================================ */

  .fotos-hero {
    background: var(--text);
    color: #fff;
    padding: 3.5rem 0 3rem;
  }
  .fotos-hero .label { color: var(--rust-mid); }
  .fotos-hero h1 {
    font-size: clamp(2rem, 5vw, 3.25rem);
    color: #fff;
    margin-bottom: 0.75rem;
  }
  .fotos-hero h1 span { color: var(--rust-mid); }
  .fotos-hero p {
    color: rgba(255,255,255,0.6);
    font-size: 1rem;
    max-width: 520px;
    margin: 0;
  }

  /* ============================================================
     FILTERS
     ============================================================ */
  .filter-bar {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 1.25rem 0;
    position: sticky;
    top: 68px;
    z-index: 50;
  }

  .filter-inner {
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .filter-group {
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .filter-label {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--text-muted);
    white-space: nowrap;
  }

  .filter-select {
    font-family: 'Inter', sans-serif;
    font-size: 0.875rem;
    color: var(--text);
    background: var(--bg);
    border: 1.5px solid var(--border);
    border-radius: var(--radius);
    padding: 0.45rem 2rem 0.45rem 0.75rem;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%237A726A' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 0.6rem center;
    cursor: pointer;
    transition: border-color var(--t);
  }
  .filter-select:focus {
    outline: none;
    border-color: var(--rust);
  }

  .filter-reset {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.75rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--text-muted);
    background: none;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.4rem 0.875rem;
    cursor: pointer;
    transition: all var(--t);
    margin-left: auto;
  }
  .filter-reset:hover {
    color: var(--rust);
    border-color: var(--rust);
    background: var(--rust-light);
  }

  .filter-count {
    font-size: 0.82rem;
    color: var(--text-muted);
    margin-left: 0.25rem;
  }
  .filter-count span {
    font-weight: 600;
    color: var(--rust);
  }

  /* ============================================================
     FOTO GRID
     ============================================================ */
  .fotos-section {
    padding: 3rem 0 5rem;
  }

  .foto-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.25rem;
  }

  .foto-card {
    background: var(--surface);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    overflow: hidden;
    transition: transform var(--t), box-shadow var(--t), border-color var(--t);
    cursor: pointer;
  }
  .foto-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 32px rgba(28,26,23,0.1);
    border-color: var(--rust-mid);
  }
  .foto-card[data-hidden="true"] { display: none; }

  .foto-thumb {
    position: relative;
    padding-bottom: 66.66%;
    overflow: hidden;
    background: var(--surface-warm);
  }
  .foto-thumb img {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    object-fit: cover;
    transition: transform 0.35s ease;
  }
  .foto-card:hover .foto-thumb img {
    transform: scale(1.04);
  }

  .foto-thumb-placeholder {
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--text-subtle);
  }
  .foto-thumb-placeholder svg { width: 36px; height: 36px; opacity: 0.35; }

  .foto-meta {
    padding: 1rem 1.125rem 1.125rem;
  }

  .foto-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-bottom: 0.625rem;
  }

  .foto-tag {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.2rem 0.55rem;
    border-radius: 100px;
  }
  .foto-tag.vervoerder { background: var(--rust-light); color: var(--rust-dark); }
  .foto-tag.type       { background: var(--forest-light); color: var(--forest); }
  .foto-tag.evenement  { background: #EEF2FF; color: #3730a3; }

  .foto-titel {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 1rem;
    color: var(--text);
    margin-bottom: 0.25rem;
    line-height: 1.3;
  }

  .foto-info {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1rem;
    margin-top: 0.5rem;
  }

  .foto-info-item {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.8rem;
    color: var(--text-muted);
  }
  .foto-info-item svg { width: 12px; height: 12px; flex-shrink: 0; opacity: 0.7; }

  /* ============================================================
     LIGHTBOX
     ============================================================ */
  .lightbox {
    display: none;
    position: fixed;
    inset: 0;
    z-index: 999;
    background: rgba(28,26,23,0.92);
    align-items: center;
    justify-content: center;
    padding: 1.5rem;
  }
  .lightbox.open { display: flex; }

  .lightbox-inner {
    position: relative;
    max-width: 1000px;
    width: 100%;
    background: var(--surface);
    border-radius: var(--radius-lg);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    max-height: 90vh;
  }

  .lightbox-img-wrap {
    position: relative;
    background: #111;
    flex-shrink: 0;
  }
  .lightbox-img-wrap img {
    width: 100%;
    max-height: 60vh;
    object-fit: contain;
    display: block;
  }

  .lightbox-close {
    position: absolute;
    top: 0.75rem;
    right: 0.75rem;
    width: 36px;
    height: 36px;
    background: rgba(0,0,0,0.5);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    transition: background var(--t);
    z-index: 2;
  }
  .lightbox-close:hover { background: var(--rust); }
  .lightbox-close svg { width: 16px; height: 16px; }

  .lightbox-body {
    padding: 1.5rem;
    overflow-y: auto;
  }

  .lightbox-title {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 1.35rem;
    color: var(--text);
    margin-bottom: 0.5rem;
  }
  .lightbox-desc {
    color: var(--text-muted);
    font-size: 0.925rem;
    margin-bottom: 1rem;
    line-height: 1.7;
  }
  .lightbox-details {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1.5rem;
    padding-top: 0.75rem;
    border-top: 1px solid var(--border);
  }
  .lightbox-detail {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.825rem;
    color: var(--text-muted);
  }
  .lightbox-detail svg { width: 13px; height: 13px; color: var(--rust); flex-shrink: 0; }
  .lightbox-detail strong { color: var(--text); font-weight: 600; }

  /* Geen resultaten */
  .no-results {
    text-align: center;
    padding: 4rem 0;
    color: var(--text-muted);
    display: none;
  }
  .no-results.visible { display: block; }
  .no-results p { font-size: 1rem; margin-top: 0.5rem; }

  /* ============================================================
     RESPONSIVE
     ============================================================ */
  @media (max-width: 600px) {
    .filter-inner { gap: 0.75rem; }
    .filter-group { width: 100%; }
    .filter-select { flex: 1; }
    .filter-reset { margin-left: 0; width: 100%; text-align: center; }
    .foto-grid { grid-template-columns: 1fr 1fr; gap: 0.75rem; }
    .lightbox-inner { border-radius: var(--radius); }
  }
  @media (max-width: 400px) {
    .foto-grid { grid-template-columns: 1fr; }
  }
</style>

<!-- HERO -->
<section class="fotos-hero">
  <div class="container">
    <p class="label">Fotodatabase</p>
    <h1>Foto's van <span>Tijmen</span></h1>
    <p>Treinen vastgelegd langs het spoor — van stoom tot hogesnelheid.</p>
  </div>
</section>

<!-- FILTER BAR -->
<div class="filter-bar">
  <div class="container">
    <div class="filter-inner">

      <div class="filter-group">
        <label class="filter-label" for="filter-vervoerder">Vervoerder</label>
        <select class="filter-select" id="filter-vervoerder">
          <option value="">Alle</option>
          <option value="ns">NS</option>
          <option value="db">DB</option>
          <option value="vsm">VSM</option>
          <option value="spoorwegmuseum">Spoorwegmuseum</option>
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label" for="filter-type">Type</label>
        <select class="filter-select" id="filter-type">
          <option value="">Alle</option>
          <option value="br193">BR 193</option>
          <option value="br52">BR 52</option>
          <option value="flirt">Flirt</option>
          <option value="ice">ICE</option>
          <option value="icng">ICNG</option>
          <option value="e-loc">E-loc</option>
          <option value="diesel">Diesel</option>
          <option value="stoom">Stoom</option>
          <option value="anders">Anders</option>
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label" for="filter-evenement">Evenement</label>
        <select class="filter-select" id="filter-evenement">
          <option value="">Alle</option>
          {% assign evenementen = site.data.fotos | map: "evenement" | uniq | sort %}
          {% for ev in evenementen %}
            {% if ev != "" and ev != nil %}
          <option value="{{ ev | downcase }}">{{ ev }}</option>
            {% endif %}
          {% endfor %}
        </select>
      </div>

      <button class="filter-reset" id="filter-reset">Wis filters</button>

      <p class="filter-count" id="filter-count">
        <span id="count-visible">{{ site.data.fotos | size }}</span> van {{ site.data.fotos | size }} foto's
      </p>

    </div>
  </div>
</div>

<!-- FOTO GRID -->
<section class="fotos-section">
  <div class="container">

    <div class="foto-grid" id="foto-grid">
      {% for foto in site.data.fotos %}
      <article class="foto-card"
               data-vervoerder="{{ foto.vervoerder | downcase | default: '' }}"
               data-type="{{ foto.type | downcase | default: '' }}"
               data-evenement="{{ foto.evenement | downcase | default: '' }}"
               onclick="openLightbox(this)">

        <div class="foto-thumb">
          <img
            src="{{ '/assets/fotos/' | append: foto.bestand | relative_url }}"
            alt="{{ foto.titel }}"
            loading="lazy"
            onerror="this.style.display='none'; this.nextElementSibling.style.display='flex';">
          <div class="foto-thumb-placeholder" style="display:none;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
              <rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/>
              <polyline points="21,15 16,10 5,21"/>
            </svg>
          </div>
        </div>

        <div class="foto-meta">
          <div class="foto-tags">
            {% if foto.vervoerder != "" and foto.vervoerder %}
            <span class="foto-tag vervoerder">{{ foto.vervoerder | upcase }}</span>
            {% endif %}
            {% if foto.type != "" and foto.type %}
            <span class="foto-tag type">{{ foto.type | upcase }}</span>
            {% endif %}
            {% if foto.evenement != "" and foto.evenement %}
            <span class="foto-tag evenement">{{ foto.evenement }}</span>
            {% endif %}
          </div>

          <h3 class="foto-titel">{{ foto.titel }}</h3>

          <div class="foto-info">
            {% if foto.datum %}
            <span class="foto-info-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>
              </svg>
              {{ foto.datum | date: "%d-%m-%Y" }}
            </span>
            {% endif %}
            {% if foto.locatie and foto.locatie != "" %}
            <span class="foto-info-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/>
              </svg>
              {{ foto.locatie }}
            </span>
            {% endif %}
            {% if foto.fotograaf and foto.fotograaf != "" %}
            <span class="foto-info-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>
              </svg>
              {{ foto.fotograaf }}
            </span>
            {% endif %}
          </div>
        </div>

        <!-- Hidden data for lightbox -->
        <script type="application/json" class="foto-data">
        {
          "bestand": "{{ foto.bestand }}",
          "titel": {{ foto.titel | jsonify }},
          "beschrijving": {{ foto.beschrijving | default: "" | jsonify }},
          "vervoerder": {{ foto.vervoerder | default: "" | jsonify }},
          "type": {{ foto.type | default: "" | jsonify }},
          "evenement": {{ foto.evenement | default: "" | jsonify }},
          "locatie": {{ foto.locatie | default: "" | jsonify }},
          "fotograaf": {{ foto.fotograaf | default: "" | jsonify }},
          "datum": {{ foto.datum | default: "" | date: "%d-%m-%Y" | jsonify }}
        }
        </script>
      </article>
      {% endfor %}
    </div>

    <div class="no-results" id="no-results">
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin:0 auto 1rem;display:block;opacity:0.3">
        <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
      </svg>
      <strong>Geen foto's gevonden</strong>
      <p>Pas de filters aan om andere foto's te zien.</p>
    </div>

  </div>
</section>

<!-- LIGHTBOX -->
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Foto vergroten">
  <div class="lightbox-inner" id="lightbox-inner">
    <div class="lightbox-img-wrap">
      <img src="" alt="" id="lightbox-img">
      <button class="lightbox-close" id="lightbox-close" aria-label="Sluiten">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
          <line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/>
        </svg>
      </button>
    </div>
    <div class="lightbox-body">
      <h2 class="lightbox-title" id="lightbox-title"></h2>
      <p class="lightbox-desc" id="lightbox-desc"></p>
      <div class="lightbox-details" id="lightbox-details"></div>
    </div>
  </div>
</div>

<script>
(function() {
  const grid        = document.getElementById('foto-grid');
  const cards       = Array.from(grid.querySelectorAll('.foto-card'));
  const noResults   = document.getElementById('no-results');
  const countEl     = document.getElementById('count-visible');
  const totalCount  = cards.length;

  const selVervoerder = document.getElementById('filter-vervoerder');
  const selType       = document.getElementById('filter-type');
  const selEvenement  = document.getElementById('filter-evenement');
  const btnReset      = document.getElementById('filter-reset');

  function applyFilters() {
    const v = selVervoerder.value;
    const t = selType.value;
    const e = selEvenement.value;
    let visible = 0;

    cards.forEach(card => {
      const match =
        (!v || card.dataset.vervoerder === v) &&
        (!t || card.dataset.type === t) &&
        (!e || card.dataset.evenement === e);

      card.dataset.hidden = match ? 'false' : 'true';
      if (match) visible++;
    });

    countEl.textContent = visible;
    noResults.classList.toggle('visible', visible === 0);
  }

  [selVervoerder, selType, selEvenement].forEach(s =>
    s.addEventListener('change', applyFilters)
  );

  btnReset.addEventListener('click', () => {
    selVervoerder.value = '';
    selType.value = '';
    selEvenement.value = '';
    applyFilters();
  });

  // ---- Lightbox ----
  const lightbox    = document.getElementById('lightbox');
  const lbImg       = document.getElementById('lightbox-img');
  const lbTitle     = document.getElementById('lightbox-title');
  const lbDesc      = document.getElementById('lightbox-desc');
  const lbDetails   = document.getElementById('lightbox-details');
  const lbClose     = document.getElementById('lightbox-close');

  window.openLightbox = function(card) {
    const raw  = card.querySelector('.foto-data').textContent;
    const data = JSON.parse(raw);
    const base = '{{ "/assets/fotos/" | relative_url }}';

    lbImg.src = base + data.bestand;
    lbImg.alt = data.titel;
    lbTitle.textContent = data.titel;
    lbDesc.textContent  = data.beschrijving || '';
    lbDesc.style.display = data.beschrijving ? '' : 'none';

    const details = [];
    if (data.vervoerder) details.push({ icon: 'train', label: 'Vervoerder', val: data.vervoerder.toUpperCase() });
    if (data.type)       details.push({ icon: 'tag',   label: 'Type',       val: data.type.toUpperCase() });
    if (data.evenement)  details.push({ icon: 'star',  label: 'Evenement',  val: data.evenement });
    if (data.locatie)    details.push({ icon: 'pin',   label: 'Locatie',    val: data.locatie });
    if (data.fotograaf)  details.push({ icon: 'cam',   label: 'Fotograaf',  val: data.fotograaf });
    if (data.datum)      details.push({ icon: 'cal',   label: 'Datum',      val: data.datum });

    const icons = {
      train: '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
      tag:   '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
      star:  '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
      pin:   '<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/>',
      cam:   '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
      cal:   '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>'
    };

    lbDetails.innerHTML = details.map(d => `
      <div class="lightbox-detail">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">${icons[d.icon]}</svg>
        <span>${d.label}: <strong>${d.val}</strong></span>
      </div>`).join('');

    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  };

  function closeLightbox() {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
    lbImg.src = '';
  }

  lbClose.addEventListener('click', closeLightbox);
  lightbox.addEventListener('click', e => {
    if (e.target === lightbox) closeLightbox();
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeLightbox();
  });
})();
</script>
