/* Explore filtering and breathing pacer. Nothing typed here is stored or sent. */
(function () {
  'use strict';

  /* ---------- Filtering over static cards ---------- */
  var form = document.querySelector('[data-explore-form]');
  if (form) {
    var cards = Array.prototype.slice.call(document.querySelectorAll('[data-explore-grid] > li'));
    var countEl = document.querySelector('[data-explore-count]');
    var emptyEl = document.querySelector('[data-explore-empty]');
    var q = form.elements.q, cat = form.elements.category, fmt = form.elements.format, age = form.elements.age;

    function apply(updateUrl) {
      var terms = q.value.toLowerCase().split(/\s+/).filter(Boolean);
      var shown = 0;
      cards.forEach(function (li) {
        var a = li.firstElementChild;
        var ok = (!cat.value || a.dataset.category === cat.value) &&
          (!fmt.value || a.dataset.format === fmt.value) &&
          (!age.value || (' ' + a.dataset.ages + ' ').indexOf(' ' + age.value + ' ') > -1) &&
          terms.every(function (t) { return a.dataset.search.indexOf(t) > -1; });
        li.hidden = !ok;
        if (ok) shown++;
      });
      var filtered = terms.length || cat.value || fmt.value || age.value;
      countEl.textContent = !filtered ? 'Showing all ' + cards.length + ' resources'
        : shown === 0 ? 'No resources found' : 'Showing ' + shown + (shown === 1 ? ' resource' : ' resources') + ' of ' + cards.length;
      emptyEl.hidden = shown !== 0;
      if (updateUrl && window.history && history.replaceState) {
        var p = new URLSearchParams();
        if (cat.value) p.set('category', cat.value);
        if (age.value) p.set('age', age.value);
        if (fmt.value) p.set('format', fmt.value);
        /* Search text is never written to the URL, so it stays out of browser history. */
        var s = p.toString();
        try { history.replaceState(null, '', location.pathname + (s ? '?' + s : '')); } catch (e) {}
      }
    }

    function setSelect(sel, v) {
      if (!v) return;
      for (var i = 0; i < sel.options.length; i++) if (sel.options[i].value === v) { sel.value = v; return; }
    }
    try {
      var params = new URLSearchParams(location.search);
      setSelect(cat, params.get('category'));
      setSelect(age, params.get('age'));
      setSelect(fmt, params.get('format'));
      q.value = params.get('q') || '';
    } catch (e) {}

    form.addEventListener('submit', function (e) { e.preventDefault(); });
    form.addEventListener('input', function () { apply(true); });
    form.addEventListener('change', function () { apply(true); });
    form.querySelector('[data-explore-reset]').addEventListener('click', function () {
      q.value = ''; cat.value = ''; fmt.value = ''; age.value = ''; apply(true); q.focus();
    });
    apply(false);
  }

  /* ---------- Breathing pacer: 4s in, 2s hold, 6s out ---------- */
  var pacer = document.querySelector('[data-breath-pacer]');
  if (pacer) {
    var circle = pacer.querySelector('[data-pacer-circle]');
    var cue = pacer.querySelector('[data-pacer-cue]');
    var btn = pacer.querySelector('[data-pacer-toggle]');
    var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
    var timer = null, running = false, rounds = 0;

    function phase(scale, secs) {
      circle.style.transitionDuration = reduce ? '0s' : secs + 's';
      circle.style.transform = reduce ? 'scale(1)' : 'scale(' + scale + ')';
    }
    function step(i) {
      if (!running) return;
      if (i === 0) { cue.textContent = 'Breathe in slowly'; phase(2.4, 4); timer = setTimeout(function () { step(1); }, 4000); }
      else if (i === 1) { cue.textContent = 'Pause gently'; timer = setTimeout(function () { step(2); }, 2000); }
      else {
        cue.textContent = 'Breathe out slowly'; phase(1, 6);
        timer = setTimeout(function () {
          rounds++;
          if (rounds >= 6) { stop('Well done. Notice how you feel. You can go again if you like.'); }
          else step(0);
        }, 6000);
      }
    }
    function stop(msg) {
      running = false; clearTimeout(timer); phase(1, 0.4);
      cue.textContent = msg || 'Stopped. Press start when you are ready.';
      btn.textContent = 'Start breathing'; btn.setAttribute('aria-pressed', 'false');
    }
    btn.addEventListener('click', function () {
      if (running) { stop(); return; }
      running = true; rounds = 0;
      btn.textContent = 'Stop'; btn.setAttribute('aria-pressed', 'true');
      step(0);
    });
  }
})();
