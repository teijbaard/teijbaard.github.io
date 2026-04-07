---
layout: default
title: "Over Tijmen"
description: "Leer Tijmen kennen: 8 jaar oud, junior treinspotter en expert op het gebied van de NS 1607, VSM 23076 en de ICE."
---

<style>
  .over-hero {
    background: var(--surface);
    padding: 4.5rem 0;
    border-bottom: 1px solid var(--border);
  }
  .over-hero-inner {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: center;
    gap: 3rem;
  }
  .over-hero h1 {
    font-size: clamp(2.75rem, 5vw, 4rem);
    color: var(--text);
    margin-bottom: 0.75rem;
    line-height: 1.05;
  }
  .over-hero h1 em { font-style: normal; color: var(--rust); }
  .over-hero p { font-size: 1.05rem; color: var(--text-muted); max-width: 420px; }
  .over-hero-logo {
    height: 140px;
    width: auto;
    flex-shrink: 0;
    opacity: 0.9;
  }

  .over-body {
    max-width: 700px;
    margin: 0 auto;
    padding: 4.5rem 1.5rem;
  }

  .over-body h2 {
    font-size: 1.85rem;
    color: var(--text);
    margin: 2.75rem 0 0.875rem;
  }
  .over-body h2:first-child { margin-top: 0; }

  .over-body p {
    color: var(--text-muted);
    font-size: 1rem;
    line-height: 1.85;
  }

  /* Quote */
  .quote-block {
    background: var(--text);
    color: #fff;
    border-radius: var(--radius-lg);
    padding: 2.5rem;
    margin: 2.5rem 0;
    position: relative;
  }
  .quote-block blockquote {
    font-size: 1.2rem;
    font-weight: 600;
    font-style: italic;
    line-height: 1.65;
    margin-bottom: 1rem;
    color: rgba(255,255,255,0.9);
  }
  .quote-block cite {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.78rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--rust-mid);
    font-style: normal;
  }

  /* Treinen grid */
  .treinen-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
    margin: 1.5rem 0;
  }

  .trein-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.375rem;
    transition: border-color var(--t), transform var(--t);
  }
  .trein-card:hover {
    border-color: var(--rust-mid);
    transform: translateY(-2px);
  }
  .trein-icon { font-size: 2rem; display: block; margin-bottom: 0.625rem; }
  .trein-name {
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 1.15rem;
    color: var(--text);
    margin-bottom: 0.4rem;
  }
  .trein-card p { font-size: 0.875rem; color: var(--text-muted); margin: 0; line-height: 1.65; }

  /* Facts list */
  .facts-list {
    list-style: none;
    padding: 0;
    display: grid;
    gap: 0.6rem;
    margin: 1.25rem 0;
  }
  .facts-list li {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.8rem 1.125rem;
    display: flex;
    align-items: center;
    gap: 0.875rem;
    font-size: 0.95rem;
    color: var(--text-muted);
  }
  .facts-list li .fi { font-size: 1.15rem; flex-shrink: 0; }

  /* Moment card */
  .moment-card {
    background: var(--rust-light);
    border: 1px solid var(--rust-mid);
    border-radius: var(--radius-lg);
    overflow: hidden;
    margin: 2rem 0;
  }
  .moment-card-img {
    width: 100%;
    max-height: 380px;
    object-fit: cover;
    display: block;
  }
  .moment-card-body {
    padding: 1.75rem 2rem;
  }
  .moment-card-body .label {
    margin-bottom: 0.75rem;
  }
  .moment-card-body h3 {
    font-size: 1.35rem;
    color: var(--text);
    margin-bottom: 0.75rem;
  }
  .moment-card-body p {
    font-size: 0.95rem;
    color: var(--text-muted);
    margin-bottom: 0.5rem;
  }
  .moment-card-credits {
    font-size: 0.78rem;
    color: var(--text-subtle);
    margin-top: 0.75rem !important;
    font-style: italic;
  }

  /* Parental notice */
  .parental-notice-box {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.5rem 2rem;
    margin-top: 3rem;
    text-align: center;
  }
  .parental-notice-box p {
    font-size: 0.875rem;
    color: var(--text-muted);
    margin: 0;
  }
  .parental-notice-box a { color: var(--rust); }

  @media (max-width: 600px) {
    .over-hero-inner { grid-template-columns: 1fr; }
    .over-hero-logo  { height: 100px; margin: 0 auto; }
    .over-body       { padding: 3rem 0; }
    .moment-card-body { padding: 1.25rem 1.5rem; }
  }
</style>

<section class="over-hero">
  <div class="container">
    <div class="over-hero-inner">
      <div>
        <span class="label">Junior treinspotter</span>
        <h1>Over <em>Tijmen</em></h1>
        <p>8 jaar oud en zo gek op treinen dat hij er 's nachts van droomt.</p>
      </div>
      <img src="{{ '/assets/img/logo.webp' | relative_url }}" alt="Tijmen op Stoom" class="over-hero-logo">
    </div>
  </div>
</section>

<div class="container">
  <div class="over-body">

    <h2>Hoe het begon</h2>
    <p>
      Toen Tijmen drie jaar oud was, stopten zijn ouders voor het eerst op het <a href="https://nl.wikipedia.org/wiki/Voetgangersbrug_Baarn" target="_blank" rel="noopener" style="color:var(--rust);">kippenbruggetje in Baarn</a> —
      een historische voetgangersbrug uit 1911, pal naast het spoor. De IC naar Berlijn
      denderde voorbij, en achter het raam van de locomotief flitste het nummer voorbij: <strong>1700</strong>.
      Tijmen stond met open mond en dacht: <em>dat wil ik ook filmen</em>.
      De 1700 werd direct zijn absolute favoriet.
    </p>
    <p>
      Elk weekend waren we te vinden op het kippenbruggetje. En al snel wilde Tijmen niet alleen
      kijken — hij wilde mee. Steeds vaker stapten hij en zijn vader samen op de trein voor een
      echte expeditie. Amsterdam Centraal werd zijn favoriete station: groot, druk en altijd
      iets te spotten. En het <strong>Spoorwegmuseum</strong> in Utrecht? Dat is voor Tijmen gewoon een tweede thuis.
    </p>

    <div class="quote-block">
      <blockquote>
        "Als een stoomlocomotief langskomt, voel je het in je buik. Dat is het vetste gevoel ter wereld!"
      </blockquote>
      <cite>— Tijmen, 8 jaar</cite>
    </div>

    <h2>Een bijzondere dag: 150 jaar Oosterspoorweg</h2>

    <div class="moment-card">
      <img
        src="{{ '/assets/img/tijmen_150_oosterspoorweg.webp' | relative_url }}"
        alt="Tijmen deelt kinderboek uit op station Baarn tijdens 150 jaar Oosterspoorweg"
        class="moment-card-img"
        loading="lazy">
      <div class="moment-card-body">
        <span class="label">8 juni 2024 · Station Baarn</span>
        <h3>Namens de NS een kinderboek uitdelen</h3>
        <p>
          Op 8 juni 2024 vierde de Oosterspoorweg zijn 150-jarig bestaan. De spoorlijn die
          al anderhalve eeuw door Baarn loopt — en waar Tijmen wekelijks op het kippenbruggetje stond —
          was ineens het middelpunt van een groot feest.
        </p>
        <p>
          Tijmen mocht die dag namens de NS op station Baarn een speciaal kinderboek uitdelen
          aan alle kinderen die langskwamen. Voor een jongen die altijd vol bewondering naar de treinen
          stond te kijken, was dit een onvergetelijk moment: nu stond hij zelf op het perron, als
          onderdeel van het feest.
        </p>
        <p class="moment-card-credits">Foto: Caspar Huurdeman</p>
      </div>
    </div>

    <h2>Mijn favoriete treinen</h2>
    <p>Er zijn veel treinen, maar deze zijn mijn absolute favorieten:</p>

    <div class="treinen-grid">
      <div class="trein-card">
        <span class="trein-icon">🟡</span>
        <div class="trein-name">NS 1607</div>
        <p>De iconische gele elektrische locomotief van NS. Tijmen vindt hem de mooiste loc van Nederland.</p>
      </div>
      <div class="trein-card">
        <span class="trein-icon">🚂</span>
        <div class="trein-name">Loc 1700</div>
        <p>De locomotief van de IC Berlijn. Het was de eerste trein die Tijmen ooit zag — en meteen zijn favoriet.</p>
      </div>
      <div class="trein-card">
        <span class="trein-icon">💨</span>
        <div class="trein-name">VSM 23076</div>
        <p>Een echte stoomlocomotief van de Veluwsche Stoomtrein Maatschappij. Hoor je dat gefluit?</p>
      </div>
      <div class="trein-card">
        <span class="trein-icon">⚡</span>
        <div class="trein-name">ICE &amp; ICNG</div>
        <p>Supersnel, supermooi en supermodern. De raketten van het spoor.</p>
      </div>
    </div>

    <h2>Fun facts</h2>
    <ul class="facts-list">
      <li><span class="fi">🎂</span> 8 jaar oud en al meer gereisd dan de meeste volwassenen</li>
      <li><span class="fi">📷</span> Filmt zelf zijn video's (met een beetje hulp van papa)</li>
      <li><span class="fi">🚉</span> Amsterdam Centraal is zijn favoriete station</li>
      <li><span class="fi">🏛️</span> Komt graag in het Spoorwegmuseum in Utrecht</li>
      <li><span class="fi">🇩🇪</span> Heeft al treinen gespot in Nederland, Duitsland en België</li>
      <li><span class="fi">📚</span> Weet het complete NS-locomotief-assortiment uit zijn hoofd</li>
      <li><span class="fi">🌙</span> Droomt letterlijk van treinen</li>
      <li><span class="fi">🏆</span> Ambitie: ooit alle stoomlocomotieven in Europa zien</li>
    </ul>

    <h2>Waarom YouTube &amp; Instagram?</h2>
    <p>
      Tijmen wil andere kinderen laten zien hoe vet treinen zijn. Via <strong>@TijmenopStoom</strong>
      neemt hij jou mee op elke expeditie. Op Instagram <strong>@TijmenOpStoom</strong> vind je
      foto's en achter-de-schermen-moments.
    </p>

    <div style="display:flex; gap:0.75rem; flex-wrap:wrap; margin-top:1.5rem;">
      <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-primary">▶ YouTube kanaal</a>
      <a href="{{ site.social.instagram }}" target="_blank" rel="noopener" class="btn btn-ghost">📸 Instagram volgen</a>
    </div>

    <div class="parental-notice-box">
      <p>
        👨‍👩‍👦 Dit platform wordt beheerd door de ouders van Tijmen.<br>
        Vragen? <a href="{{ '/contact' | relative_url }}">Neem contact op</a>.
      </p>
    </div>

  </div>
</div>
