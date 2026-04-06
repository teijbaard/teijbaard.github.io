---
layout: default
title: "Home"
description: "Ik ben Tijmen (8) en gek op treinen! Volg mijn avonturen langs stoomtreinen, ICE en goederentreinen."
---

<style>
  /* ============================================================
     HOME PAGE
     ============================================================ */

  /* Hero */
  .hero {
    background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy-mid) 60%, #1e4d7a 100%);
    color: var(--white);
    padding: 5rem 0 4rem;
    text-align: center;
    position: relative;
    overflow: hidden;
  }

  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background:
      radial-gradient(ellipse 70% 80% at 50% 110%, rgba(232,160,32,0.12) 0%, transparent 70%),
      repeating-linear-gradient(
        0deg,
        transparent 0px,
        transparent 40px,
        rgba(255,255,255,0.015) 40px,
        rgba(255,255,255,0.015) 41px
      );
    pointer-events: none;
  }

  .hero-logo-wrap {
    position: relative;
    display: inline-block;
    margin-bottom: 2rem;
  }

  .hero-logo {
    height: 180px;
    width: auto;
    filter: drop-shadow(0 8px 32px rgba(0,0,0,0.5));
    animation: logo-float 4s ease-in-out infinite;
  }

  @keyframes logo-float {
    0%, 100% { transform: translateY(0); }
    50%       { transform: translateY(-8px); }
  }

  .hero-tagline {
    font-family: 'Bebas Neue', cursive;
    font-size: clamp(2.5rem, 7vw, 5rem);
    line-height: 1;
    margin-bottom: 0.5rem;
    color: var(--white);
  }
  .hero-tagline span { color: var(--ochre); }

  .hero-sub {
    font-size: 1.15rem;
    color: rgba(255,255,255,0.75);
    max-width: 480px;
    margin: 0 auto 2rem;
    font-weight: 600;
  }

  .hero-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }

  /* Stats strip */
  .stats-strip {
    background: var(--ochre);
    color: var(--navy-dark);
    padding: 1rem 0;
  }
  .stats-inner {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 2.5rem;
    flex-wrap: wrap;
  }
  .stat {
    text-align: center;
    font-family: 'Bebas Neue', cursive;
  }
  .stat-number {
    font-size: 2rem;
    line-height: 1;
    display: block;
  }
  .stat-label {
    font-size: 0.75rem;
    letter-spacing: 0.12em;
    opacity: 0.8;
  }
  .stat-divider {
    width: 1px;
    height: 36px;
    background: rgba(26,58,92,0.25);
  }

  /* Sections */
  .home-section {
    padding: 4rem 0;
  }

  .section-heading {
    font-size: clamp(2rem, 4vw, 3rem);
    color: var(--navy-dark);
    margin-bottom: 0.5rem;
  }

  /* Video section */
  .video-section {
    background: var(--navy-dark);
    padding: 4rem 0;
    color: var(--white);
  }
  .video-section .section-heading { color: var(--white); }

  .video-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    align-items: center;
    margin-top: 2rem;
  }

  .video-text p { color: rgba(255,255,255,0.8); font-size: 1.05rem; margin-bottom: 1.5rem; }

  /* Expedities preview */
  .expedities-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
  }

  .expeditie-card {
    background: var(--white);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow);
    transition: transform var(--transition), box-shadow var(--transition);
    display: flex;
    flex-direction: column;
  }
  .expeditie-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
  }

  .card-header {
    background: var(--navy);
    color: var(--white);
    padding: 1.25rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 1rem;
  }
  .card-number {
    font-family: 'Bebas Neue', cursive;
    font-size: 2.5rem;
    color: var(--ochre);
    line-height: 1;
    flex-shrink: 0;
  }
  .card-title-wrap { flex: 1; }
  .card-title {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.4rem;
    line-height: 1.2;
    display: block;
  }
  .card-date {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.6);
    margin-top: 0.2rem;
  }

  .card-body { padding: 1.25rem 1.5rem; flex: 1; }
  .card-body p { font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1rem; }

  /* Instagram / social block */
  .social-block {
    background: linear-gradient(135deg, #833AB4, #FD1D1D 50%, #FCAF45);
    color: var(--white);
    border-radius: var(--radius-lg);
    padding: 3rem 2rem;
    text-align: center;
  }
  .social-block h2 {
    font-family: 'Bebas Neue', cursive;
    font-size: 2.5rem;
    margin-bottom: 0.75rem;
  }
  .social-block p { opacity: 0.9; margin-bottom: 1.5rem; }

  /* Welcome band */
  .welcome-band {
    background: var(--ochre-pale);
    border-top: 4px solid var(--ochre);
    border-bottom: 4px solid var(--ochre);
    padding: 3rem 0;
    text-align: center;
  }
  .welcome-band h2 {
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    color: var(--navy-dark);
    margin-bottom: 0.75rem;
  }
  .welcome-band p {
    font-size: 1.1rem;
    color: var(--navy);
    max-width: 540px;
    margin: 0 auto;
    font-weight: 600;
  }

  @media (max-width: 640px) {
    .video-grid { grid-template-columns: 1fr; }
    .hero-logo { height: 140px; }
  }
</style>

<!-- ========================================================
     HERO
     ======================================================== -->
<section class="hero">
  <div class="container">
    <div class="hero-logo-wrap">
      <div class="steam-container">
        <div class="steam-puff"></div>
        <div class="steam-puff"></div>
        <div class="steam-puff"></div>
      </div>
      <img src="{{ '/assets/img/logo.webp' | relative_url }}" alt="Tijmen op Stoom" class="hero-logo">
    </div>

    <h1 class="hero-tagline">Tijmen <span>op Stoom</span></h1>
    <p class="hero-sub">Ik ben Tijmen (8) en gek op treinen! Stoom, ICE, ICNG — ik mis er geen één.</p>

    <div class="hero-actions">
      <a href="{{ '/expedities' | relative_url }}" class="btn btn-primary">
        🚂 Bekijk mijn expedities
      </a>
      <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-outline">
        ▶ YouTube kanaal
      </a>
    </div>
  </div>
</section>

<!-- Stats -->
<div class="stats-strip">
  <div class="container">
    <div class="stats-inner">
      <div class="stat">
        <span class="stat-number">8</span>
        <span class="stat-label">Jaar oud</span>
      </div>
      <div class="stat-divider"></div>
      <div class="stat">
        <span class="stat-number">18+</span>
        <span class="stat-label">Expedities</span>
      </div>
      <div class="stat-divider"></div>
      <div class="stat">
        <span class="stat-number">NS&nbsp;1607</span>
        <span class="stat-label">Favoriete loc</span>
      </div>
      <div class="stat-divider"></div>
      <div class="stat">
        <span class="stat-number">🇩🇪 🇳🇱 🇧🇪</span>
        <span class="stat-label">Landen bezocht</span>
      </div>
    </div>
  </div>
</div>

<!-- ========================================================
     LAATSTE VIDEO
     ======================================================== -->
<section class="video-section">
  <div class="container">
    <span class="section-label">🎬 Nieuwste video</span>
    <div class="video-grid">
      <div class="video-text">
        <h2 class="section-heading">Laatste Video</h2>
        <p>
          Wil je mee op avontuur? Op mijn YouTube-kanaal zie je alles: stoomtreinen die puffen en blazen,
          superschelle ICE's en lange goederentreinen. Abonneer je en mis geen enkele rit!
        </p>
        <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-primary">
          <svg viewBox="0 0 24 24" fill="currentColor" width="18" height="18"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          Abonneer je nu
        </a>
      </div>
      <div>
        <!-- Vervang VIDEO_ID met het YouTube video ID van de laatste video -->
        <div class="video-wrapper">
          <iframe
            src="https://www.youtube.com/embed?listType=user_uploads&list=TijmenopStoom"
            title="Laatste video van Tijmen op Stoom"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            loading="lazy">
          </iframe>
        </div>
        <p style="color:rgba(255,255,255,0.4); font-size:0.8rem; margin-top:0.5rem; text-align:center;">
          💡 Tip: vervang de embed-URL met het ID van jouw nieuwste video
        </p>
      </div>
    </div>
  </div>
</section>

<!-- ========================================================
     WELKOMSTBERICHT
     ======================================================== -->
<section class="welcome-band">
  <div class="container">
    <h2>Welkom op het spoor! 🚂</h2>
    <p>
      Ik ben Tijmen, 8 jaar oud en de grootste treinliefhebber die je ooit zult tegenkomen.
      Of het nou een stoomlocomotief is die door de Veluwe raast of een ICE die door Duitsland scheurt —
      ik sta erbij en ik film het allemaal. Ga jij mee op expeditie?
    </p>
  </div>
</section>

<!-- ========================================================
     EXPEDITIES PREVIEW
     ======================================================== -->
<section class="home-section bg-white">
  <div class="container">
    <span class="section-label">🗺️ Mijn avonturen</span>
    <h2 class="section-heading">Recente Expedities</h2>

    <div class="expedities-grid">
      {% for expeditie in site.expedities limit:3 %}
      <article class="expeditie-card">
        <div class="card-header">
          <span class="card-number">{{ expeditie.nummer | default: "01" }}</span>
          <div class="card-title-wrap">
            <span class="card-title">{{ expeditie.title }}</span>
            <span class="card-date">{{ expeditie.date | date: "%-d %B %Y" }}</span>
          </div>
        </div>
        <div class="card-body">
          <p>{{ expeditie.excerpt | strip_html | truncate: 100 }}</p>
          <a href="{{ expeditie.url | relative_url }}" class="btn btn-navy" style="font-size:0.95rem; padding:0.6rem 1.25rem;">
            Lees meer →
          </a>
        </div>
      </article>
      {% endfor %}
    </div>

    <div class="text-center mt-lg">
      <a href="{{ '/expedities' | relative_url }}" class="btn btn-primary">
        Alle expedities bekijken
      </a>
    </div>
  </div>
</section>

<!-- ========================================================
     INSTAGRAM / SOCIAL
     ======================================================== -->
<section class="home-section">
  <div class="container">
    <div class="social-block">
      <h2>📸 Volg m'n avontuur</h2>
      <p>
        Foto's, behind-the-scenes en spontane treinspots — alles staat op Instagram.<br>
        Volg <strong>@TijmenOpStoom</strong> en mis geen enkel moment!
      </p>
      <a href="{{ site.social.instagram }}" target="_blank" rel="noopener" class="btn" style="background:white; color:#833AB4; font-size:1.1rem;">
        <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
        Volg @TijmenOpStoom
      </a>
    </div>
  </div>
</section>
