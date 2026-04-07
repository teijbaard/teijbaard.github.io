---
layout: default
title: "Contact"
description: "Neem contact op met Tijmen op Stoom. Dit platform wordt beheerd door de ouders van Tijmen."
---

<style>
  .contact-hero {
    background: var(--surface);
    padding: 4.5rem 0;
    border-bottom: 1px solid var(--border);
  }
  .contact-hero h1 {
    font-size: clamp(2.75rem, 5vw, 4rem);
    color: var(--text);
    margin-bottom: 0.75rem;
  }
  .contact-hero h1 em { font-style: normal; color: var(--rust); }
  .contact-hero p { color: var(--text-muted); max-width: 400px; }

  .contact-body {
    max-width: 680px;
    margin: 0 auto;
    padding: 4.5rem 1.5rem;
    display: grid;
    gap: 1.5rem;
  }

  .contact-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 2rem 2.25rem;
  }

  .contact-card h2 {
    font-size: 1.5rem;
    color: var(--text);
    margin-bottom: 0.75rem;
  }

  .contact-card p {
    color: var(--text-muted);
    font-size: 0.975rem;
    line-height: 1.8;
    margin-bottom: 1.25rem;
  }

  .contact-form label {
    display: block;
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.85rem;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--text);
    margin-bottom: 0.4rem;
  }
  .contact-form input,
  .contact-form textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 1.5px solid var(--border);
    border-radius: var(--radius);
    background: var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
    font-size: 0.975rem;
    transition: border-color var(--t), box-shadow var(--t);
  }
  .contact-form input:focus,
  .contact-form textarea:focus {
    outline: none;
    border-color: var(--rust);
    box-shadow: 0 0 0 3px rgba(192,78,26,0.1);
  }
  .contact-form textarea { resize: vertical; min-height: 130px; }
  .contact-form .form-group { margin-bottom: 1.25rem; }
  .contact-form .form-group:last-of-type { margin-bottom: 1.5rem; }
  .contact-form .submit-btn {
    width: 100%;
    justify-content: center;
    font-size: 1rem;
    padding: 0.9rem;
  }
  .contact-form .submit-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
  }

  .social-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.75rem;
    margin-top: 1.25rem;
  }

  .social-btn-lg {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.875rem;
    border-radius: var(--radius);
    font-family: 'Fira Sans', sans-serif;
    font-weight: 800;
    font-size: 0.875rem;
    color: #fff;
    transition: all var(--t);
  }
  .social-btn-lg.yt { background: #FF0000; }
  .social-btn-lg.yt:hover { background: #CC0000; transform: translateY(-1px); }
  .social-btn-lg.ig { background: linear-gradient(135deg, #833AB4, #FD1D1D, #FCAF45); }
  .social-btn-lg.ig:hover { opacity: 0.88; transform: translateY(-1px); }
  .social-btn-lg svg { width: 18px; height: 18px; }

  .parental-card {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.75rem 2.25rem;
    text-align: center;
  }
  .parental-card p {
    font-size: 0.875rem;
    color: var(--text-muted);
    margin: 0;
    line-height: 1.75;
  }

  @media (max-width: 500px) {
    .social-grid { grid-template-columns: 1fr; }
    .contact-card { padding: 1.5rem; }
  }
</style>

<section class="contact-hero">
  <div class="container">
    <span class="label">Neem contact op</span>
    <h1>Stuur een <em>berichtje</em></h1>
    <p>Vragen, opmerkingen of gewoon even zeggen dat je de videos leuk vindt? Wij horen graag van je.</p>
  </div>
</section>

<div class="container">
  <div class="contact-body">

    <div class="contact-card">
      <h2>✉️ Stuur een bericht</h2>
      <p>
        Heb je een vraag of reactie? Vul het formulier in en we reageren zo snel mogelijk.
        Alle berichten worden gelezen en beantwoord door de ouders van Tijmen.
      </p>
      <!-- Webhook: vervang de action-URL door jouw eigen Make.com webhook -->
      <form id="contact-form" class="contact-form" action="{{ site.make_webhook_url }}" method="POST">
        <div class="form-group">
          <label for="name">Naam</label>
          <input type="text" id="name" name="name" required placeholder="Jouw naam">
        </div>
        <div class="form-group">
          <label for="email">E-mailadres</label>
          <input type="email" id="email" name="_replyto" required placeholder="jouw@email.nl">
        </div>
        <div class="form-group">
          <label for="message">Bericht</label>
          <textarea id="message" name="message" required placeholder="Schrijf hier je bericht…"></textarea>
        </div>
        <button id="submit-btn" type="submit" class="btn btn-primary submit-btn">Versturen</button>
      </form>
      <script>
        document.getElementById('contact-form').addEventListener('submit', function(e) {
          e.preventDefault();
          var btn = document.getElementById('submit-btn');
          btn.disabled = true;
          btn.textContent = 'Bezig met verzenden…';
          fetch(this.action, { method: 'POST', body: new FormData(this) })
            .finally(function() { window.location.href = '/bedankt/'; });
        });
      </script>
    </div>

    <div class="contact-card">
      <h2>📱 Sociale media</h2>
      <p>
        Voor snelle berichten ben je ook welkom op onze sociale kanalen.
        Stuur een DM op Instagram of reageer op een video.
      </p>
      <div class="social-grid">
        <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="social-btn-lg yt">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          @TijmenopStoom
        </a>
        <a href="{{ site.social.instagram }}" target="_blank" rel="noopener" class="social-btn-lg ig">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"/></svg>
          @TijmenOpStoom
        </a>
      </div>
    </div>

    <div class="parental-card">
      <p>
        👨‍👩‍👦 <strong>Tijmen is 8 jaar oud.</strong> Dit platform wordt volledig beheerd door zijn ouders.
        Alle communicatie verloopt via de ouders. Tijmen beantwoordt zelf geen berichten van onbekenden.
      </p>
    </div>

  </div>
</div>
