---
layout: default
title: "Even geen stoom"
description: "De website is tijdelijk niet beschikbaar. We zijn zo terug!"
permalink: /onderhoud/
sitemap: false
---

<style>
  .onderhoud-hero {
    background: var(--surface);
    padding: 5rem 0 4rem;
    border-bottom: 1px solid var(--border);
    text-align: center;
  }

  .onderhoud-title {
    font-size: clamp(2.5rem, 5vw, 3.75rem);
    color: var(--text);
    margin-bottom: 1rem;
    line-height: 1.05;
  }
  .onderhoud-title em {
    font-style: normal;
    color: var(--rust);
  }

  .onderhoud-lead {
    font-size: 1.05rem;
    color: var(--text-muted);
    max-width: 480px;
    margin: 0 auto 2.5rem;
  }

  .onderhoud-img {
    width: 100%;
    max-width: 420px;
    border-radius: var(--radius-lg);
    box-shadow: 0 12px 40px rgba(28,26,23,0.12);
    margin: 0 auto 2.5rem;
    display: block;
  }
</style>

<section class="onderhoud-hero">
  <div class="container">
    <span class="label">Even geen stoom</span>
    <h1 class="onderhoud-title">We zijn zo<br>weer <em>op de rails</em>!</h1>
    <p class="onderhoud-lead">
      De website is tijdelijk niet beschikbaar in verband met onderhoud.
      We zijn hard aan het werk en zijn zo snel mogelijk terug. Bedankt voor je geduld!
    </p>
    <a href="{{ site.social.youtube }}" target="_blank" rel="noopener" class="btn btn-primary">
      <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
      Bekijk ondertussen YouTube
    </a>
  </div>
</section>
