---
layout: default
title: "Foto's"
description: "Alle foto's van Tijmen op Stoom — gefilterd op vervoerder, treinstel, land of evenement."
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
    padding: 1rem 0;
    position: sticky;
    top: 68px;
    z-index: 50;
  }

  .filter-inner {
    display: flex;
    align-items: center;
    gap: 0.75rem 1rem;
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

  .filter-select,
  .filter-search {
    font-family: 'Inter', sans-serif;
    font-size: 0.875rem;
    color: var(--text);
    background: var(--bg);
    border: 1.5px solid var(--border);
    border-radius: var(--radius);
    padding: 0.45rem 0.75rem;
    transition: border-color var(--t);
  }
  .filter-select {
    padding-right: 2rem;
    appearance: none;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%237A726A' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-position: right 0.6rem center;
    cursor: pointer;
  }
  .filter-select:hover { border-color: var(--rust-mid); }
  .filter-search { min-width: 12rem; }
  .filter-select:focus,
  .filter-search:focus { border-color: var(--rust); }

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
    margin: 0;
  }
  .filter-count span {
    font-weight: 600;
    color: var(--rust);
  }

  /* ============================================================
     FOTO GRID
     ============================================================ */
  .fotos-section { padding: 3rem 0 5rem; }

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
  .foto-card:hover .foto-thumb img { transform: scale(1.04); }

  .foto-meta { padding: 1rem 1.125rem 1.125rem; }

  .foto-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-bottom: 0.625rem;
  }

  .foto-tag {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.68rem;
    letter-spacing: 0.03em;
    padding: 0.2rem 0.55rem;
    border-radius: 100px;
  }
  .foto-tag.vervoerder { background: var(--rust-light);   color: var(--rust-dark); }
  .foto-tag.type       { background: var(--forest-light); color: var(--forest); }
  .foto-tag.evenement  { background: #EEF2FF;             color: #3730a3; }

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
     BEHEER — alleen zichtbaar op /fotos/?beheer=1
     ============================================================ */
  .beheer-uitleg { display: none; }
  body.beheer .beheer-uitleg {
    display: block;
    background: var(--rust-light);
    border: 1px solid var(--rust-mid);
    border-radius: var(--radius);
    padding: 1rem 1.25rem;
    margin-bottom: 1.75rem;
    font-size: 0.875rem;
    color: var(--rust-dark);
  }
  .beheer-uitleg code {
    background: rgba(255,255,255,0.6);
    padding: 0.05rem 0.35rem;
    border-radius: 4px;
    font-size: 0.85em;
  }

  .kies-header {
    display: none;
    position: absolute;
    top: 0.6rem;
    left: 0.6rem;
    z-index: 2;
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.68rem;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #fff;
    background: rgba(28,26,23,0.72);
    border: none;
    border-radius: 100px;
    padding: 0.3rem 0.7rem;
    cursor: pointer;
    transition: background var(--t);
  }
  body.beheer .foto-card[data-hero="true"] .kies-header { display: block; }
  .kies-header:hover { background: var(--rust); }
  .kies-header[data-huidig="true"] { background: var(--forest); }

  .beheer-toast {
    position: fixed;
    left: 50%;
    bottom: 1.5rem;
    transform: translateX(-50%);
    z-index: 900;
    max-width: min(92vw, 34rem);
    background: var(--text);
    color: #fff;
    border-radius: var(--radius-lg);
    padding: 1.125rem 1.25rem;
    box-shadow: 0 12px 40px rgba(0,0,0,0.3);
    font-size: 0.85rem;
    line-height: 1.6;
  }
  .beheer-toast[hidden] { display: none; }
  .beheer-toast pre {
    background: rgba(255,255,255,0.08);
    border-radius: var(--radius);
    padding: 0.6rem 0.75rem;
    margin: 0.6rem 0;
    overflow-x: auto;
    font-size: 0.75rem;
    line-height: 1.5;
  }
  .beheer-toast a { color: var(--rust-mid); text-decoration: underline; }
  .beheer-toast button {
    background: none;
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    border-radius: var(--radius);
    padding: 0.25rem 0.7rem;
    font-size: 0.75rem;
    cursor: pointer;
    margin-top: 0.35rem;
  }

  /* Geen resultaten */
  .no-results {
    text-align: center;
    padding: 4rem 0;
    color: var(--text-muted);
  }
  .no-results[hidden] { display: none; }
  .no-results p { font-size: 1rem; margin-top: 0.5rem; }

  /* ============================================================
     RESPONSIVE
     ============================================================ */
  @media (max-width: 600px) {
    /* Vier filters onder elkaar duwt de foto's van het scherm af; in twee
       kolommen met het label erboven past de hele balk in één blik. */
    .filter-bar   { padding: 0.75rem 0; }
    .filter-inner {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.6rem 0.75rem;
      align-items: end;
    }
    .filter-group {
      flex-direction: column;
      align-items: stretch;
      gap: 0.25rem;
      min-width: 0;
    }
    .filter-select, .filter-search { width: 100%; min-width: 0; }
    .filter-group:has(.filter-search),
    .filter-reset,
    .filter-count { grid-column: 1 / -1; }
    .filter-reset { margin-left: 0; text-align: center; }
    .filter-count { text-align: center; }
    .foto-grid    { grid-template-columns: 1fr 1fr; gap: 0.75rem; }
    .foto-meta    { padding: 0.75rem 0.875rem 0.875rem; }
    .foto-titel   { font-size: 0.9rem; }
  }
  @media (max-width: 400px) {
    .foto-grid { grid-template-columns: 1fr; }
  }
</style>

{%- assign fotos = site.data.fotos -%}
{%- assign labels = site.data.labels -%}

<!-- HERO -->
<section class="fotos-hero">
  <div class="container">
    <p class="label">Fotodatabase</p>
    <h1>Foto's van <span>Tijmen</span></h1>
    <p>Treinen vastgelegd langs het spoor — van stoom tot hogesnelheid.</p>
  </div>
</section>

<!-- FILTER BAR -->
{%- comment -%}
  De keuzemenu's worden opgebouwd uit de data zelf. Komt er een nieuwe
  vervoerder of een nieuw type in _data/fotos.yml, dan staat die hier vanzelf —
  de weergavenaam komt uit _data/labels.yml.
{%- endcomment -%}
<div class="filter-bar">
  <div class="container">
    <div class="filter-inner">

      <div class="filter-group">
        <label class="filter-label" for="filter-vervoerder">Vervoerder</label>
        <select class="filter-select" id="filter-vervoerder" data-veld="vervoerder">
          <option value="">Alle</option>
          {%- assign vervoerders = fotos | map: "vervoerder" | compact | uniq | sort -%}
          {%- for v in vervoerders -%}
            {%- if v != "" and v -%}
              {%- assign aantal = fotos | where: "vervoerder", v | size -%}
          <option value="{{ v }}">{{ labels.vervoerder[v] | default: v }} ({{ aantal }})</option>
            {%- endif -%}
          {%- endfor -%}
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label" for="filter-type">Type</label>
        <select class="filter-select" id="filter-type" data-veld="type">
          <option value="">Alle</option>
          {%- assign types = fotos | map: "type" | compact | uniq | sort -%}
          {%- for ty in types -%}
            {%- if ty != "" and ty -%}
              {%- assign aantal = fotos | where: "type", ty | size -%}
          <option value="{{ ty }}">{{ labels.type[ty] | default: ty }} ({{ aantal }})</option>
            {%- endif -%}
          {%- endfor -%}
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label" for="filter-land">Land</label>
        <select class="filter-select" id="filter-land" data-veld="land">
          <option value="">Alle</option>
          {%- assign landen = fotos | map: "land" | compact | uniq | sort -%}
          {%- for l in landen -%}
            {%- if l != "" and l -%}
              {%- assign aantal = fotos | where: "land", l | size -%}
          <option value="{{ l }}">{{ labels.land[l] | default: l }} ({{ aantal }})</option>
            {%- endif -%}
          {%- endfor -%}
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label" for="filter-evenement">Evenement</label>
        <select class="filter-select" id="filter-evenement" data-veld="evenement">
          <option value="">Alle</option>
          {%- assign evenementen = fotos | map: "evenement" | compact | uniq | sort -%}
          {%- for ev in evenementen -%}
            {%- if ev != "" and ev -%}
              {%- assign aantal = fotos | where: "evenement", ev | size -%}
          <option value="{{ ev | downcase }}">{{ ev }} ({{ aantal }})</option>
            {%- endif -%}
          {%- endfor -%}
        </select>
      </div>

      <div class="filter-group">
        <label class="filter-label sr-only" for="filter-zoek">Zoeken</label>
        <input class="filter-search" id="filter-zoek" type="search"
               placeholder="Zoek op titel of plaats…" autocomplete="off">
      </div>

      <button class="filter-reset" id="filter-reset" type="button">Wis filters</button>

      <p class="filter-count" aria-live="polite">
        <span id="count-visible">{{ fotos | size }}</span> van {{ fotos | size }} foto's
      </p>

    </div>
  </div>
</div>

<!-- FOTO GRID -->
<section class="fotos-section">
  <div class="container">

    <div class="beheer-uitleg">
      <strong>Beheermodus.</strong> Bij elke liggende foto staat nu een knop
      <em>Maak header</em>. Die zet de inhoud van <code>_data/hero.yml</code> op je
      klembord — plakken en committen, en de foto staat een week op de homepage.
      Daarna kiest de wekelijkse Action zelf een andere.
    </div>

    <h2 class="sr-only">Alle foto's</h2>
    <div class="foto-grid" id="foto-grid">
      {%- for foto in fotos %}
      {%- assign basis = foto.bestand | split: ".webp" | first %}
      <article class="foto-card"
               data-vervoerder="{{ foto.vervoerder | downcase }}"
               data-type="{{ foto.type | downcase }}"
               data-land="{{ foto.land | downcase }}"
               data-evenement="{{ foto.evenement | downcase }}"
               data-hero="{{ foto.hero }}"
               data-zoek="{{ foto.titel | append: ' ' | append: foto.locatie | append: ' ' | append: foto.evenement | append: ' ' | append: foto.beschrijving | downcase | escape }}">

        <div class="foto-thumb">
          <img src="{{ '/assets/fotos/' | append: basis | append: '-thumb.webp' | relative_url }}"
               srcset="{{ '/assets/fotos/' | append: basis | append: '-thumb.webp' | relative_url }} 640w,
                       {{ '/assets/fotos/' | append: foto.bestand | relative_url }} 1800w"
               sizes="(max-width: 400px) 100vw, (max-width: 600px) 50vw, (max-width: 1080px) 33vw, 340px"
               alt="{{ foto.titel | escape }}"
               width="{{ foto.breedte }}" height="{{ foto.hoogte }}"
               loading="lazy" decoding="async">
          {%- if foto.hero %}
          <button type="button" class="kies-header"
                  data-bestand="{{ foto.bestand }}"
                  data-titel="{{ foto.titel | escape }}">Maak header</button>
          {%- endif %}
        </div>

        <div class="foto-meta">
          <div class="foto-tags">
            {%- if foto.vervoerder != "" and foto.vervoerder %}
            <span class="foto-tag vervoerder">{{ labels.vervoerder[foto.vervoerder] | default: foto.vervoerder }}</span>
            {%- endif %}
            {%- if foto.type != "" and foto.type %}
            <span class="foto-tag type">{{ labels.type[foto.type] | default: foto.type }}</span>
            {%- endif %}
            {%- if foto.evenement != "" and foto.evenement %}
            <span class="foto-tag evenement">{{ foto.evenement }}</span>
            {%- endif %}
          </div>

          <h3 class="foto-titel">
            <button type="button" class="foto-open">{{ foto.titel }}</button>
          </h3>

          <div class="foto-info">
            {%- if foto.datum and foto.datum != "" %}
            <span class="foto-info-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
                <rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>
              </svg>
              {% include datum.html d=foto.datum kort=true %} {{ foto.datum | date: "%Y" }}
            </span>
            {%- endif %}
            {%- if foto.locatie and foto.locatie != "" %}
            <span class="foto-info-item">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
                <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/>
              </svg>
              {{ foto.locatie }}
            </span>
            {%- endif %}
          </div>
        </div>

        <script type="application/json" class="foto-data">
        {
          "bestand": {{ foto.bestand | jsonify }},
          "titel": {{ foto.titel | jsonify }},
          "beschrijving": {{ foto.beschrijving | default: "" | jsonify }},
          "vervoerder": {{ labels.vervoerder[foto.vervoerder] | default: foto.vervoerder | default: "" | jsonify }},
          "type": {{ labels.type[foto.type] | default: foto.type | default: "" | jsonify }},
          "evenement": {{ foto.evenement | default: "" | jsonify }},
          "locatie": {{ foto.locatie | default: "" | jsonify }},
          "fotograaf": {{ foto.fotograaf | default: site.author.name | jsonify }},
          "datum": {% capture d %}{% include datum.html d=foto.datum %}{% endcapture %}{{ d | jsonify }}
        }
        </script>
      </article>
      {%- endfor %}
    </div>

    <div class="no-results" id="no-results" hidden>
      <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="margin:0 auto 1rem;display:block;opacity:0.3" aria-hidden="true">
        <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
      </svg>
      <strong>Geen foto's gevonden</strong>
      <p>Pas de filters aan om andere foto's te zien.</p>
    </div>

  </div>
</section>

<div class="beheer-toast" id="beheer-toast" hidden></div>

{% include lightbox.html %}

<script>
(function () {
  'use strict';

  var grid      = document.getElementById('foto-grid');
  var kaarten   = Array.prototype.slice.call(grid.querySelectorAll('.foto-card'));
  var geenHits  = document.getElementById('no-results');
  var teller    = document.getElementById('count-visible');
  var zoekveld  = document.getElementById('filter-zoek');
  var resetKnop = document.getElementById('filter-reset');
  var selects   = Array.prototype.slice.call(document.querySelectorAll('.filter-select'));

  function pasToe() {
    var term = zoekveld.value.trim().toLowerCase();
    var zichtbaar = 0;

    kaarten.forEach(function (kaart) {
      var match = selects.every(function (s) {
        return !s.value || kaart.dataset[s.dataset.veld] === s.value;
      }) && (!term || kaart.dataset.zoek.indexOf(term) !== -1);

      kaart.dataset.hidden = match ? 'false' : 'true';
      if (match) zichtbaar++;
    });

    teller.textContent = zichtbaar;
    geenHits.hidden = zichtbaar > 0;
    bewaarInUrl();
  }

  // Filters staan in de URL, zodat je een selectie kunt delen en de knop
  // "Alle foto's bekijken" op een expeditiepagina meteen goed uitkomt.
  function bewaarInUrl() {
    var p = new URLSearchParams();
    selects.forEach(function (s) { if (s.value) p.set(s.dataset.veld, s.value); });
    if (zoekveld.value.trim()) p.set('zoek', zoekveld.value.trim());
    // Beheermodus vasthouden, anders verdwijnt hij bij de eerste filterwijziging
    // en is de pagina niet meer als beheer-URL te delen of te herladen.
    if (document.body.classList.contains('beheer')) p.set('beheer', '1');
    var q = p.toString();
    history.replaceState(null, '', q ? '?' + q : location.pathname);
  }

  function leesUitUrl() {
    var p = new URLSearchParams(location.search);
    selects.forEach(function (s) {
      var v = (p.get(s.dataset.veld) || '').toLowerCase();
      if (!v) return;
      // Alleen instellen als de waarde echt bestaat, anders blijft het leeg.
      var treffer = Array.prototype.find.call(s.options, function (o) {
        return o.value.toLowerCase() === v;
      });
      if (treffer) s.value = treffer.value;
    });
    zoekveld.value = p.get('zoek') || '';
    if (p.get('beheer') === '1') document.body.classList.add('beheer');
  }

  selects.forEach(function (s) { s.addEventListener('change', pasToe); });
  zoekveld.addEventListener('input', pasToe);
  resetKnop.addEventListener('click', function () {
    selects.forEach(function (s) { s.value = ''; });
    zoekveld.value = '';
    pasToe();
  });

  leesUitUrl();
  pasToe();

  // ---- Beheer: headerfoto kiezen ----
  var toast = document.getElementById('beheer-toast');
  var vandaag = new Date().toISOString().slice(0, 10);
  var repo = {{ site.repository | default: "" | jsonify }};

  document.addEventListener('click', function (e) {
    var knop = e.target.closest('.kies-header');
    if (!knop) return;
    e.preventDefault();
    e.stopPropagation();

    var yaml = [
      'bestand:      "' + knop.dataset.bestand + '"',
      'ingesteld_op: "' + vandaag + '"',
      'bron:         "handmatig"',
      'vast:         false'
    ].join('\n');

    var bewerkUrl = repo ? 'https://github.com/' + repo + '/edit/main/_data/hero.yml' : '';
    toast.hidden = false;
    toast.innerHTML =
      '<strong>' + knop.dataset.titel + '</strong> als headerfoto.' +
      '<pre>' + yaml.replace(/</g, '&lt;') + '</pre>' +
      'Vervang hiermee de vier regels bovenin <code>_data/hero.yml</code>' +
      (bewerkUrl ? ' — <a href="' + bewerkUrl + '" target="_blank" rel="noopener">open op GitHub</a>' : '') +
      '.<br><button type="button" id="toast-dicht">Sluiten</button>';

    if (navigator.clipboard) {
      navigator.clipboard.writeText(yaml).then(function () {
        toast.insertAdjacentHTML('afterbegin', '<div style="color:#8FCFA8">✓ Naar klembord gekopieerd</div>');
      }, function () { /* klembord geweigerd — de tekst staat er toch */ });
    }
    document.getElementById('toast-dicht').addEventListener('click', function () {
      toast.hidden = true;
    });
  });
})();
</script>
