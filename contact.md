---
layout: default
title: "Contact"
description: "Zakelijke aanvragen voor Tijmen op Stoom? Neem contact op via e-mail. Dit platform wordt beheerd door de ouders van Tijmen."
---

<style>
  .contact-hero {
    background: linear-gradient(135deg, var(--navy-dark) 0%, var(--navy-mid) 100%);
    color: var(--white);
    padding: 4rem 0;
    text-align: center;
  }
  .contact-hero h1 {
    font-size: clamp(3rem, 7vw, 5rem);
    color: var(--white);
    margin-bottom: 0.5rem;
  }
  .contact-hero h1 span { color: var(--ochre); }
  .contact-hero p { color: rgba(255,255,255,0.7); max-width: 480px; margin: 0 auto; }

  .contact-layout {
    max-width: 760px;
    margin: 0 auto;
    padding: 4rem 1.25rem;
    display: grid;
    gap: 2rem;
  }

  .contact-card {
    background: var(--white);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow);
    padding: 2.5rem;
    border-top: 5px solid var(--ochre);
  }

  .contact-card h2 {
    font-size: 2rem;
    color: var(--navy-dark);
    margin-bottom: 1rem;
  }

  .contact-card p {
    font-size: 1rem;
    color: var(--text-muted);
    line-height: 1.8;
    margin-bottom: 1.25rem;
  }

  .email-display {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    background: var(--navy-dark);
    color: var(--ochre);
    font-family: 'Bebas Neue', cursive;
    font-size: 1.3rem;
    letter-spacing: 0.08em;
    padding: 1rem 1.75rem;
    border-radius: var(--radius);
    transition: all var(--transition);
    text-decoration: none;
  }
  .email-display:hover {
    background: var(--navy-mid);
    transform: translateY(-2px);
    box-shadow: var(--shadow);
  }
  .email-display svg { flex-shrink: 0; }

  .contact-rules {
    background: var(--ochre-pale);
    border-radius: var(--radius-lg);
    border: 2px solid var(--ochre-light);
    padding: 2rem 2.5rem;
  }
  .contact-rules h2 {
    font-size: 1.8rem;
    color: var(--navy-dark);
    margin-bottom: 1rem;
  }
  .contact-rules ul {
    list-style: none;
    padding: 0;
    display: grid;
    gap: 0.6rem;
  }
  .contact-rules li {
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    font-size: 0.95rem;
    color: var(--navy);
    font-weight: 600;
  }
  .contact-rules li::before {
    content: '✓';
    color: var(--ochre);
    font-weight: 900;
    flex-shrink: 0;
    margin-top: 0.1rem;
  }

  .response-time {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    background: var(--navy-dark);
    color: rgba(255,255,255,0.85);
    padding: 1rem 1.5rem;
    border-radius: var(--radius);
    margin-top: 1.5rem;
    font-size: 0.9rem;
    font-weight: 600;
  }
  .response-time .icon { font-size: 1.25rem; flex-shrink: 0; }

  .parental-box {
    background: var(--off-white);
    border-radius: var(--radius-lg);
    border: 2px dashed var(--ochre);
    padding: 2rem;
    text-align: center;
  }
  .parental-box .big-icon { font-size: 2.5rem; display: block; margin-bottom: 0.75rem; }
  .parental-box p { font-size: 0.9rem; color: var(--text-muted); line-height: 1.7; margin: 0; }
  .parental-box strong { color: var(--navy-dark); }

  .social-contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-top: 1.5rem;
  }

  .social-contact-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.6rem;
    padding: 1rem;
    border-radius: var(--radius);
    font-family: 'Bebas Neue', cursive;
    font-size: 1.1rem;
    letter-spacing: 0.06em;
    transition: all var(--transition);
    color: white;
  }
  .social-contact-btn.yt { background: #FF0000; }
  .social-contact-btn.yt:hover { background: #CC0000; transform: translateY(-2px); }
  .social-contact-btn.ig { background: linear-gradient(135deg, #833AB4, #FD1D1D, #FCAF45); }
  .social-contact-btn.ig:hover { opacity: 0.9; transform: translateY(-2px); }
  .social-contact-btn svg { width: 20px; height: 20px; }

  @media (max-width: 500px) {
    .social-contact-grid { grid-template-columns: 1fr; }
    .contact-card { padding: 1.5rem; }
  }
</style>

<section class="contact-hero">
  <div class="container">
    <h1>Get in <span>Touch</span></h1>
    <p>Zakelijke vragen, samenwerkingen of gewoon hoi zeggen? Wij horen graag van je!</p>
  </div>
</section>
<div class="track-line"></div>

<div class="contact-layout">

  <!-- E-mail -->
  <div class="contact-card">
    <h2>📧 Zakelijke Aanvragen</h2>
    <p>
      Voor samenwerkingen, sponsoring, evenementen of media-aanvragen kun je ons bereiken via e-mail.
      Alle berichten worden gelezen en beantwoord door de ouders van Tijmen.
    </p>
    <a href="mailto:info@tijmenopstoom.nl" class="email-display">
      <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22">
        <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
      </svg>
      info@tijmenopstoom.nl
    </a>
    <div class="response-time">
      <span class="icon">⏱️</span>
      We proberen binnen 3–5 werkdagen te reageren.
    </div>
  </div>

  <!-- Waar we wel/niet voor zijn -->
  <div class="contact-rules">
    <h2>💼 Wat we doen</h2>
    <ul>
      <li>Samenwerkingen met trein- en reisgerelateerde merken</li>
      <li>Product reviews van treingerelateerde items (boeken, modelbouw, merch)</li>
      <li>Gastbijdragen of vermeldingen op family-friendly platformen</li>
      <li>Evenementen en persevenementen rondom treinen en spoor</li>
      <li>Media-aanvragen en interviews</li>
    </ul>
  </div>

  <!-- Sociale media -->
  <div class="contact-card">
    <h2>📱 Sociale Media</h2>
    <p>
      Voor snelle berichtjes en reacties ben je ook welkom op onze sociale kanalen.
      Stuur een DM op Instagram of reageer op een video — Tijmen's ouders lezen alles!
    </p>
    <div class="social-contact-grid">
      <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="social-contact-btn yt">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
        YouTube
      </a>
      <a href="{{ site.social.instagram }}" target="_blank" rel="noopener" class="social-contact-btn ig">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
        Instagram
      </a>
    </div>
  </div>

  <!-- Parental notice -->
  <div class="parental-box">
    <span class="big-icon">👨‍👩‍👦</span>
    <p>
      <strong>Opmerking voor ouders &amp; verzorgers:</strong><br>
      Tijmen is 8 jaar oud. Dit platform — inclusief alle sociale media — wordt volledig beheerd
      door zijn ouders. Alle communicatie verloopt via de ouders. Tijmen beantwoordt zelf geen
      berichten van onbekenden.
    </p>
  </div>

</div>
