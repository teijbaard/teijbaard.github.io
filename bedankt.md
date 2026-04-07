---
layout: default
title: "Bedankt!"
description: "Je bericht is ontvangen. We nemen zo snel mogelijk contact op."
---

<section class="contact-hero" style="text-align:center;">
  <div class="container">
    <span class="label">Bericht verzonden</span>
    <h1>Bedankt voor je <em>berichtje</em>!</h1>
    <p>We hebben je bericht goed ontvangen en reageren zo snel mogelijk.</p>
    <div style="margin-top:2rem; display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
      <a href="{{ '/' | relative_url }}" class="btn btn-primary">← Terug naar home</a>
      <a href="{{ '/expedities' | relative_url }}" class="btn btn-ghost">Bekijk de expedities</a>
    </div>
  </div>
</section>

<style>
  .contact-hero {
    background: var(--surface);
    padding: 6rem 0;
    border-bottom: 1px solid var(--border);
  }
  .contact-hero h1 {
    font-size: clamp(2.75rem, 5vw, 4rem);
    color: var(--text);
    margin-bottom: 0.75rem;
  }
  .contact-hero h1 em { font-style: normal; color: var(--rust); }
  .contact-hero p { color: var(--text-muted); max-width: 400px; margin: 0 auto; }
</style>
