---
layout: default
title: "Over Tijmen"
description: "Leer Tijmen kennen: 8 jaar oud, junior treinspotter en expert op het gebied van de NS 1607, VSM 23076 en de ICE."
---

<style>
  .over-hero {
    background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy-mid) 100%);
    color: var(--white);
    padding: 4rem 0;
    text-align: center;
  }
  .over-hero h1 {
    font-size: clamp(3rem, 7vw, 5.5rem);
    color: var(--white);
    margin-bottom: 0.5rem;
  }
  .over-hero h1 span { color: var(--ochre); }
  .over-hero p { color: rgba(255,255,255,0.75); font-size: 1.1rem; max-width: 480px; margin: 0 auto; }

  .about-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 4rem 1.25rem;
  }

  .about-content h2 {
    font-size: clamp(2rem, 4vw, 3rem);
    color: var(--navy-dark);
    margin: 2.5rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
  }

  .about-content p {
    font-size: 1.05rem;
    line-height: 1.85;
    color: #2a2a3e;
  }

  /* Train cards */
  .trein-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1.25rem;
    margin: 2rem 0;
  }

  .trein-card {
    background: var(--white);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow);
    padding: 1.5rem;
    border-top: 4px solid var(--ochre);
    transition: transform var(--transition);
  }
  .trein-card:hover { transform: translateY(-3px); }

  .trein-icon {
    font-size: 2.5rem;
    margin-bottom: 0.75rem;
    display: block;
  }

  .trein-name {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.5rem;
    color: var(--navy-dark);
    margin-bottom: 0.5rem;
    letter-spacing: 0.05em;
  }

  .trein-card p {
    font-size: 0.9rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin: 0;
  }

  /* Quote block */
  .tijmen-quote {
    background: var(--navy-dark);
    color: var(--white);
    border-radius: var(--radius-lg);
    padding: 2.5rem;
    margin: 3rem 0;
    position: relative;
    overflow: hidden;
  }
  .tijmen-quote::before {
    content: '"';
    font-family: 'Bebas Neue', cursive;
    font-size: 12rem;
    color: rgba(232,160,32,0.12);
    position: absolute;
    top: -2rem;
    left: 1rem;
    line-height: 1;
    pointer-events: none;
  }
  .tijmen-quote blockquote {
    font-size: 1.3rem;
    font-weight: 700;
    font-style: italic;
    color: var(--white);
    position: relative;
    z-index: 1;
    margin-bottom: 1rem;
    line-height: 1.6;
  }
  .tijmen-quote cite {
    color: var(--ochre);
    font-family: 'Bebas Neue', cursive;
    font-size: 1rem;
    letter-spacing: 0.1em;
    font-style: normal;
  }

  /* Fun facts */
  .facts-list {
    list-style: none;
    padding: 0;
    display: grid;
    gap: 0.75rem;
    margin: 1.5rem 0;
  }
  .facts-list li {
    background: var(--white);
    border-radius: var(--radius);
    padding: 0.9rem 1.25rem;
    box-shadow: var(--shadow);
    display: flex;
    align-items: center;
    gap: 1rem;
    font-size: 1rem;
    font-weight: 600;
  }
  .facts-list li .fact-icon {
    font-size: 1.4rem;
    flex-shrink: 0;
  }

  /* Parental notice */
  .parental-footer-box {
    background: var(--ochre-pale);
    border: 2px solid var(--ochre);
    border-radius: var(--radius-lg);
    padding: 1.5rem 2rem;
    margin-top: 3rem;
    text-align: center;
  }
  .parental-footer-box p {
    color: var(--navy-dark);
    font-weight: 700;
    font-size: 0.95rem;
    margin: 0;
  }
  .parental-footer-box .icon { font-size: 1.75rem; display: block; margin-bottom: 0.5rem; }
</style>

<!-- Hero -->
<section class="over-hero">
  <div class="container">
    <img src="{{ '/assets/img/logo.webp' | relative_url }}" alt="Tijmen op Stoom" style="height:120px; margin:0 auto 1.5rem;">
    <h1>Over <span>Tijmen</span></h1>
    <p>Junior treinspotter, 8 jaar oud en zo gek op treinen dat hij er 's nachts van droomt.</p>
  </div>
</section>

<div class="track-line"></div>

<div class="about-content">

  <h2>🚂 Hoe het begon</h2>
  <p>
    Toen Tijmen drie jaar oud was, stopten zijn ouders voor het eerst bij een spoorovergang. Een lange goederentrein denderde voorbij — wagon na wagon, het geluid leek nooit te stoppen. Tijmen stond met open mond en dacht: <em>dat wil ik ook filmen</em>.
  </p>
  <p>
    Sindsdien is er geen weekend voorbijgegaan zonder een treinspot. Van het perron in Utrecht Centraal tot de dampende rails van museumspoorwegen — Tijmen staat overal.
  </p>

  <!-- Quote -->
  <div class="tijmen-quote">
    <blockquote>
      "Als een stoomlocomotief langs komt, voel je het in je buik. Dat is het vetste gevoel ter wereld!"
    </blockquote>
    <cite>— Tijmen, 8 jaar</cite>
  </div>

  <h2>🌟 Mijn favoriete treinen</h2>
  <p>Er zijn veel treinen, maar deze drie zijn echt <strong>mijn absolute favorieten</strong>:</p>

  <div class="trein-grid">
    <div class="trein-card">
      <span class="trein-icon">🟡</span>
      <div class="trein-name">NS 1607</div>
      <p>
        De iconische gele elektrische locomotief van NS. Tijmen vindt hem de mooiste loc van Nederland — dat geel straalt als de zon!
      </p>
    </div>
    <div class="trein-card">
      <span class="trein-icon">💨</span>
      <div class="trein-name">VSM 23076</div>
      <p>
        Een echte stoomlocomotief van de Veluwsche Stoomtrein Maatschappij. Hoor je dat gefluit? Dan is Tijmen er al bij!
      </p>
    </div>
    <div class="trein-card">
      <span class="trein-icon">⚡</span>
      <div class="trein-name">ICE & ICNG</div>
      <p>
        Supersnel, supermooi en supermodern. De hogesnelheidstreinen van Deutsche Bahn zijn voor Tijmen de raketten van het spoor.
      </p>
    </div>
  </div>

  <h2>📋 Fun Facts over Tijmen</h2>
  <ul class="facts-list">
    <li><span class="fact-icon">🎂</span> 8 jaar oud en al meer gereisd dan de meeste volwassenen</li>
    <li><span class="fact-icon">📷</span> Filmt zelf zijn video's (met een beetje hulp van papa)</li>
    <li><span class="fact-icon">🇩🇪</span> Heeft al treinen gespot in Nederland, Duitsland en België</li>
    <li><span class="fact-icon">📚</span> Weet het complete NS-locomotief-assortiment uit zijn hoofd</li>
    <li><span class="fact-icon">🌙</span> Droomt letterlijk van treinen</li>
    <li><span class="fact-icon">🏆</span> Ambitie: ooit alle stoomlocomotiven in Europa zien</li>
  </ul>

  <h2>🎬 Waarom YouTube & Instagram?</h2>
  <p>
    Tijmen wil andere kinderen laten zien hoe vet treinen zijn. Veel kids kennen alleen de intercity — maar er is zóveel meer: stoom, geluid, snelheid, geschiedenis. Via zijn kanaal <strong>@TijmenopStoom</strong> neemt hij jou mee op elke expeditie.
  </p>
  <p>
    Op Instagram <strong>@TijmenOpStoom</strong> vind je de foto's, achter-de-schermen-moments en spontane treinspots.
  </p>

  <div style="display:flex; gap:1rem; flex-wrap:wrap; margin-top:1.5rem;">
    <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-primary">
      ▶ YouTube kanaal
    </a>
    <a href="{{ site.social.instagram }}" target="_blank" rel="noopener" class="btn btn-navy">
      📸 Instagram volgen
    </a>
  </div>

  <!-- Parental notice -->
  <div class="parental-footer-box">
    <span class="icon">👨‍👩‍👦</span>
    <p>Dit platform wordt beheerd door de ouders van Tijmen.<br>
    Voor zakelijke aanvragen, samenwerking of vragen: <a href="{{ '/contact' | relative_url }}" style="color:var(--navy); text-decoration:underline;">zie de contactpagina</a>.</p>
  </div>

</div>
