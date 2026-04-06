---
layout: default
title: "Home"
description: "Ik ben Tijmen (8) en gek op treinen! Volg mijn avonturen langs stoomtreinen, ICE en goederentreinen."
---

<style>
  /* =====================================================
     HOME — HERO
     ===================================================== */
  .hero {
    background: var(--surface);
    padding: 5rem 0 4rem;
    border-bottom: 1px solid var(--border);
  }

  .hero-inner {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .hero-text .label { margin-bottom: 1.25rem; }

  .hero-title {
    font-size: clamp(2.8rem, 5.5vw, 4.5rem);
    color: var(--text);
    margin-bottom: 1.25rem;
    line-height: 1.05;
  }
  .hero-title em {
    font-style: normal;
    color: var(--rust);
  }

  .hero-lead {
    font-size: 1.1rem;
    color: var(--text-muted);
    margin-bottom: 2rem;
    max-width: 420px;
  }

  .hero-actions {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
  }

  .hero-visual {
    display: flex;
    justify-content: center;
    position: relative;
  }

  .hero-logo-wrap {
    position: relative;
    display: inline-block;
  }

  .hero-logo {
    height: 240px;
    width: auto;
    filter: drop-shadow(0 12px 32px rgba(28,26,23,0.12));
    animation: float 5s ease-in-out infinite;
  }

  @keyframes float {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(-10px); }
  }

  /* =====================================================
     NUMBERS BAR
     ===================================================== */
  .numbers-bar {
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    padding: 1.5rem 0;
  }

  .numbers-inner {
    display: flex;
    justify-content: center;
    gap: 0;
    flex-wrap: wrap;
  }

  .number-item {
    text-align: center;
    padding: 0.75rem 2.5rem;
    border-right: 1px solid var(--border);
  }
  .number-item:last-child { border-right: none; }

  .number-value {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 1.75rem;
    color: var(--rust);
    display: block;
    line-height: 1;
    margin-bottom: 0.25rem;
  }

  .number-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-weight: 500;
  }

  /* =====================================================
     VIDEO SECTION
     ===================================================== */
  .video-section {
    padding: 5rem 0;
    background: var(--bg);
  }

  .video-inner {
    display: grid;
    grid-template-columns: 1fr 1.2fr;
    gap: 4rem;
    align-items: center;
  }

  .video-text h2 {
    font-size: clamp(2rem, 3.5vw, 2.8rem);
    color: var(--text);
    margin-bottom: 1rem;
  }

  .video-text p {
    color: var(--text-muted);
    margin-bottom: 1.75rem;
    font-size: 1.025rem;
  }

  /* =====================================================
     WELCOME
     ===================================================== */
  .welcome-section {
    background: var(--rust);
    padding: 4.5rem 0;
    text-align: center;
    color: #fff;
  }

  .welcome-section h2 {
    font-size: clamp(2rem, 4vw, 3rem);
    color: #fff;
    margin-bottom: 1rem;
  }

  .welcome-section p {
    font-size: 1.05rem;
    opacity: 0.88;
    max-width: 540px;
    margin: 0 auto;
  }

  /* =====================================================
     EXPEDITIES PREVIEW
     ===================================================== */
  .expedities-section {
    padding: 5rem 0;
    background: var(--surface);
    border-top: 1px solid var(--border);
  }

  .section-header {
    margin-bottom: 2.5rem;
  }

  .section-header h2 {
    font-size: clamp(2rem, 3.5vw, 2.75rem);
    color: var(--text);
  }

  .exp-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.25rem;
  }

  .exp-card {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    text-decoration: none;
    color: inherit;
    display: flex;
    flex-direction: column;
    transition: transform var(--t), border-color var(--t), box-shadow var(--t);
  }
  .exp-card:hover {
    transform: translateY(-3px);
    border-color: var(--rust-mid);
    box-shadow: 0 8px 24px rgba(28,26,23,0.07);
  }

  .exp-card-head {
    background: var(--text);
    padding: 1.25rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .exp-num {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 2.25rem;
    color: var(--rust-mid);
    line-height: 1;
    flex-shrink: 0;
  }

  .exp-card-title {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 1.1rem;
    color: #fff;
    line-height: 1.25;
  }

  .exp-card-date {
    font-size: 0.78rem;
    color: rgba(255,255,255,0.45);
    margin-top: 0.2rem;
  }

  .exp-card-body {
    padding: 1.25rem 1.5rem;
    flex: 1;
    display: flex;
    flex-direction: column;
  }

  .exp-card-body p {
    font-size: 0.9rem;
    color: var(--text-muted);
    flex: 1;
    margin-bottom: 1rem;
  }

  .exp-card-body .btn {
    align-self: flex-start;
    font-size: 0.8rem;
    padding: 0.5rem 1rem;
  }

  .section-footer {
    margin-top: 2.5rem;
    text-align: center;
  }

  /* =====================================================
     INSTAGRAM BLOCK
     ===================================================== */
  .instagram-section {
    padding: 5rem 0;
    background: var(--bg);
    border-top: 1px solid var(--border);
  }

  .instagram-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 3.5rem;
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 3rem;
  }

  .instagram-card h2 {
    font-size: clamp(1.75rem, 3vw, 2.5rem);
    color: var(--text);
    margin-bottom: 0.75rem;
  }

  .instagram-card p {
    color: var(--text-muted);
    font-size: 1rem;
    margin-bottom: 1.5rem;
  }

  .ig-big-icon {
    font-size: 5rem;
    line-height: 1;
    opacity: 0.2;
    flex-shrink: 0;
  }

  /* =====================================================
     RESPONSIVE
     ===================================================== */
  @media (max-width: 768px) {
    .hero-inner    { grid-template-columns: 1fr; gap: 2.5rem; }
    .hero-visual   { order: -1; }
    .hero-logo     { height: 180px; }
    .video-inner   { grid-template-columns: 1fr; gap: 2rem; }
    .instagram-card { grid-template-columns: 1fr; }
    .ig-big-icon   { display: none; }
    .number-item   { padding: 0.75rem 1.25rem; }
  }

  @media (max-width: 480px) {
    .hero { padding: 3.5rem 0 3rem; }
    .numbers-inner { justify-content: flex-start; }
    .number-item { border-right: none; border-bottom: 1px solid var(--border); width: 50%; }
  }
</style>

<!-- HERO -->
<section class="hero">
  <div class="container">
    <div class="hero-inner">
      <div class="hero-text">
        <span class="label">Junior treinspotter · 8 jaar</span>
        <h1 class="hero-title">Op avontuur<br>langs de <em>rails</em></h1>
        <p class="hero-lead">
          Ik ben Tijmen en ik spot treinen van Nederland tot Duitsland.
          Stoom, ICE, ICNG, goederentreinen — ik mis er geen één.
        </p>
        <div class="hero-actions">
          <a href="{{ '/expedities' | relative_url }}" class="btn btn-primary">Mijn expedities</a>
          <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-outline">▶ YouTube</a>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-logo-wrap">
          <div class="steam-wrap">
            <div class="steam-puff"></div>
            <div class="steam-puff"></div>
            <div class="steam-puff"></div>
          </div>
          <img src="{{ '/assets/img/logo.webp' | relative_url }}" alt="Tijmen op Stoom" class="hero-logo">
        </div>
      </div>
    </div>
  </div>
</section>

<!-- NUMBERS -->
<div class="numbers-bar">
  <div class="container">
    <div class="numbers-inner">
      <div class="number-item">
        <span class="number-value">8</span>
        <span class="number-label">Jaar oud</span>
      </div>
      <div class="number-item">
        <span class="number-value">18+</span>
        <span class="number-label">Expedities</span>
      </div>
      <div class="number-item">
        <span class="number-value">NS 1607</span>
        <span class="number-label">Favoriete loc</span>
      </div>
      <div class="number-item">
        <span class="number-value">🇳🇱 🇩🇪 🇧🇪</span>
        <span class="number-label">Landen</span>
      </div>
    </div>
  </div>
</div>

<!-- VIDEO -->
<section class="video-section">
  <div class="container">
    <div class="video-inner">
      <div class="video-text">
        <span class="label">Nieuwste video</span>
        <h2>Bekijk mijn<br>laatste rit</h2>
        <p>
          Elke expeditie staat op YouTube. Van stoomtreinen die puffen en blazen
          tot superschelle ICE's — abonneer je en mis niets.
        </p>
        <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-primary">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          Abonneer op YouTube
        </a>
      </div>
      <div>
        <div class="video-wrapper">
          <iframe
            src="https://www.youtube.com/embed?listType=user_uploads&list=TijmenopStoom"
            title="Laatste video van Tijmen op Stoom"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            loading="lazy">
          </iframe>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- WELCOME -->
<section class="welcome-section">
  <div class="container">
    <h2>Welkom op het spoor 🚂</h2>
    <p>
      Of het nou een stoomlocomotief is die door de Veluwe raast of een ICE die door Duitsland scheurt —
      ik sta erbij en ik film het. Ga je mee op expeditie?
    </p>
  </div>
</section>

<!-- EXPEDITIES -->
<section class="expedities-section">
  <div class="container">
    <div class="section-header">
      <span class="label">Avonturen</span>
      <h2>Recente expedities</h2>
    </div>

    <div class="exp-grid">
      {% for expeditie in site.expedities limit:3 %}
      <a href="{{ expeditie.url | relative_url }}" class="exp-card">
        <div class="exp-card-head">
          <span class="exp-num">{{ expeditie.nummer | default: forloop.index }}</span>
          <div>
            <div class="exp-card-title">{{ expeditie.title }}</div>
            <div class="exp-card-date">{{ expeditie.date | date: "%-d %B %Y" }}</div>
          </div>
        </div>
        <div class="exp-card-body">
          <p>{{ expeditie.excerpt | strip_html | truncate: 100 }}</p>
          <span class="btn btn-ghost">Lees meer →</span>
        </div>
      </a>
      {% endfor %}
    </div>

    <div class="section-footer">
      <a href="{{ '/expedities' | relative_url }}" class="btn btn-primary">Alle expedities bekijken</a>
    </div>
  </div>
</section>

<!-- INSTAGRAM -->
<section class="instagram-section">
  <div class="container">
    <div class="instagram-card">
      <div>
        <span class="label">Instagram</span>
        <h2>Volg m'n avontuur</h2>
        <p>
          Foto's, behind-the-scenes en spontane treinspots staan op Instagram.
          Volg <strong>@TijmenOpStoom</strong> en mis geen enkel moment.
        </p>
        <a href="{{ site.social.instagram }}" target="_blank" rel="noopener" class="btn btn-forest">
          <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
          Volg @TijmenOpStoom
        </a>
      </div>
      <div class="ig-big-icon" aria-hidden="true">📸</div>
    </div>
  </div>
</section>
