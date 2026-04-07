---
layout: default
title: "Bedankt!"
description: "Je bericht is ontvangen. We nemen zo snel mogelijk contact op."
---

<style>
  .bedankt-hero {
    background: var(--surface);
    padding: 5rem 0 4rem;
    border-bottom: 1px solid var(--border);
  }

  .bedankt-inner {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }

  .bedankt-text .label { margin-bottom: 1.25rem; }

  .bedankt-title {
    font-size: clamp(2.5rem, 5vw, 3.75rem);
    color: var(--text);
    margin-bottom: 1rem;
    line-height: 1.05;
  }
  .bedankt-title em {
    font-style: normal;
    color: var(--rust);
  }

  .bedankt-lead {
    font-size: 1.05rem;
    color: var(--text-muted);
    margin-bottom: 2rem;
    max-width: 420px;
  }

  .bedankt-actions {
    display: flex;
    gap: 0.75rem;
    flex-wrap: wrap;
  }

  .bedankt-visual {
    display: flex;
    justify-content: center;
  }

  .bedankt-img {
    width: 100%;
    max-width: 420px;
    border-radius: var(--radius-lg);
    box-shadow: 0 12px 40px rgba(28,26,23,0.12);
  }

  @media (max-width: 768px) {
    .bedankt-inner { grid-template-columns: 1fr; gap: 2.5rem; }
    .bedankt-visual { order: -1; }
    .bedankt-lead { max-width: 100%; }
  }
</style>

<section class="bedankt-hero">
  <div class="container">
    <div class="bedankt-inner">
      <div class="bedankt-text">
        <span class="label">Bericht verzonden</span>
        <h1 class="bedankt-title">Bedankt voor je <em>berichtje</em>!</h1>
        <p class="bedankt-lead">
          Je bericht is goed aangekomen. De ouders van Tijmen nemen zo snel mogelijk contact met je op.
        </p>
        <div class="bedankt-actions">
          <a href="{{ '/' | relative_url }}" class="btn btn-primary">← Terug naar home</a>
          <a href="{{ '/expedities' | relative_url }}" class="btn btn-ghost">Bekijk de expedities</a>
        </div>
      </div>
      <div class="bedankt-visual">
        <img src="{{ '/assets/img/bedankt.webp' | relative_url }}" alt="Bericht verzonden" class="bedankt-img" loading="lazy">
      </div>
    </div>
  </div>
</section>
