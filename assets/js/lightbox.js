/* Lightbox voor de fotokaarten — gedeeld door /fotos/ en de expedities.
 *
 * Werkt op elke <article class="foto-card"> die een knop .foto-open bevat en
 * een <script type="application/json" class="foto-data"> met de gegevens.
 * Bladeren gaat alleen langs de kaarten die op dat moment zichtbaar zijn, dus
 * een actief filter geldt ook binnen de lightbox.
 */
(function () {
  'use strict';

  var doos = document.getElementById('lightbox');
  if (!doos) return;

  var basis    = (document.currentScript || document.querySelector('script[data-basis]'))
                   .dataset.basis || '/assets/fotos/';
  var afb      = document.getElementById('lightbox-img');
  var titel    = document.getElementById('lightbox-title');
  var tekst    = document.getElementById('lightbox-desc');
  var details  = document.getElementById('lightbox-details');
  var sluitBtn = document.getElementById('lightbox-close');
  var vorigeBtn = document.getElementById('lightbox-prev');
  var volgendeBtn = document.getElementById('lightbox-next');

  var kaarten = [];   // zichtbare kaarten op het moment van openen
  var index = -1;
  var herkomst = null; // element dat de focus terugkrijgt

  var iconen = {
    train: '<path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/>',
    tag:   '<path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/>',
    star:  '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
    pin:   '<path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/>',
    cam:   '<path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/>',
    cal:   '<rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/>'
  };

  function ontsnap(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  function zichtbareKaarten(kaart) {
    var houder = kaart.closest('.foto-grid, .exp-fotos-grid') || document;
    return Array.prototype.filter.call(
      houder.querySelectorAll('.foto-card'),
      function (k) { return k.dataset.hidden !== 'true'; }
    );
  }

  function toon(i) {
    var kaart = kaarten[i];
    if (!kaart) return;
    index = i;

    var data = JSON.parse(kaart.querySelector('.foto-data').textContent);
    afb.src = basis + data.bestand;
    afb.alt = data.titel;
    titel.textContent = data.titel;
    tekst.textContent = data.beschrijving || '';
    tekst.hidden = !data.beschrijving;

    var rijen = [];
    if (data.vervoerder) rijen.push(['train', 'Vervoerder', data.vervoerder]);
    if (data.type)       rijen.push(['tag',   'Type',       data.type]);
    if (data.evenement)  rijen.push(['star',  'Evenement',  data.evenement]);
    if (data.locatie)    rijen.push(['pin',   'Locatie',    data.locatie]);
    if (data.fotograaf)  rijen.push(['cam',   'Fotograaf',  data.fotograaf]);
    if (data.datum)      rijen.push(['cal',   'Datum',      data.datum]);

    details.innerHTML = rijen.map(function (r) {
      return '<div class="lightbox-detail">' +
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">' +
        iconen[r[0]] + '</svg><span>' + r[1] + ': <strong>' + ontsnap(r[2]) + '</strong></span></div>';
    }).join('');

    var meerdere = kaarten.length > 1;
    vorigeBtn.hidden = volgendeBtn.hidden = !meerdere;
  }

  function open(kaart) {
    kaarten = zichtbareKaarten(kaart);
    var i = kaarten.indexOf(kaart);
    if (i < 0) { kaarten = [kaart]; i = 0; }

    // Bij sluiten gaat de focus terug naar de knop van deze kaart. Niet naar
    // document.activeElement: dat is <body> als de lightbox via script opent.
    herkomst = kaart.querySelector('.foto-open') || document.activeElement;
    doos.hidden = false;
    document.body.style.overflow = 'hidden';
    toon(i);
    sluitBtn.focus();
  }

  function sluit() {
    doos.hidden = true;
    document.body.style.overflow = '';
    afb.removeAttribute('src');
    if (herkomst && herkomst.focus) herkomst.focus();
    herkomst = null;
  }

  function stap(richting) {
    if (kaarten.length < 2) return;
    toon((index + richting + kaarten.length) % kaarten.length);
  }

  // Eén luisteraar voor alle kaarten, ook die later worden toegevoegd.
  document.addEventListener('click', function (e) {
    var knop = e.target.closest('.foto-open');
    if (!knop) return;
    var kaart = knop.closest('.foto-card');
    if (kaart) { e.preventDefault(); open(kaart); }
  });

  sluitBtn.addEventListener('click', sluit);
  vorigeBtn.addEventListener('click', function () { stap(-1); });
  volgendeBtn.addEventListener('click', function () { stap(1); });
  doos.addEventListener('click', function (e) { if (e.target === doos) sluit(); });

  document.addEventListener('keydown', function (e) {
    if (doos.hidden) return;
    if (e.key === 'Escape')     { sluit(); }
    else if (e.key === 'ArrowLeft')  { stap(-1); }
    else if (e.key === 'ArrowRight') { stap(1); }
    else if (e.key === 'Tab') {
      // Focus binnen de dialoog houden zolang die openstaat.
      var focusbaar = Array.prototype.filter.call(
        doos.querySelectorAll('button'), function (b) { return !b.hidden; });
      var eerste = focusbaar[0];
      var laatste = focusbaar[focusbaar.length - 1];
      if (e.shiftKey && document.activeElement === eerste) { e.preventDefault(); laatste.focus(); }
      else if (!e.shiftKey && document.activeElement === laatste) { e.preventDefault(); eerste.focus(); }
    }
  });
})();
