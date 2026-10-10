/* Logo review hub: shared menu bar, shared shortlist and owner notes.
   Included by every board with <script src=".../hub-menu.js" data-board="key"></script>,
   placed after the board's own script. Plain JS, no dependencies. */
(function () {
  'use strict';

  var KEY = 'uap-logo-shortlist';

  /* Boards in browsing order. Paths are relative to hub.html. */
  var BOARDS = [
    { key: 'feeling', name: 'Feeling board', path: '../references/feeling-board.html' },
    { key: 'type', name: 'Type board', path: 'typeboard/index.html' },
    { key: 'round1', name: 'Round 1', path: 'index.html' },
    { key: 'round2', name: 'Round 2', path: 'round2/index.html' },
    { key: 'round3', name: 'Round 3', path: 'round3/index.html' },
    { key: 'round4', name: 'Round 4', path: 'round4/index.html' },
    { key: 'round5', name: 'Round 5', path: 'round5/index.html' },
    { key: 'round6', name: 'Round 6', path: 'round6/index.html' },
    { key: 'round7tiles', name: 'Round 7 tiles', path: 'round7/tiles/index.html' },
    { key: 'round7triangles', name: 'Round 7 triangles', path: 'round7/triangles/index.html' },
    { key: 'shortlist', name: 'Shortlist', path: 'shortlist/index.html' },
    { key: 'final', name: 'Final', path: 'final/index.html' }
  ];
  /* Pages that carry the menu but sit outside the browsing order. */
  var EXTRA = {
    hub: { name: 'All boards', prev: null, next: 'feeling' },
    round7: { name: 'Round 7', prev: 'round6', next: 'round7tiles' }
  };

  var script = document.currentScript;
  var boardKey = script ? script.getAttribute('data-board') : null;
  var hubUrl = new URL('hub.html', script ? script.src : location.href);

  function boardByKey(k) {
    for (var i = 0; i < BOARDS.length; i++) { if (BOARDS[i].key === k) { return BOARDS[i]; } }
    return null;
  }
  function boardUrl(b) { return new URL(b.path, hubUrl).href; }
  function boardDir(b) { var p = b.path; return p.slice(0, p.lastIndexOf('/') + 1); }

  /* ---------- storage (every access guarded; falls back to memory) ---------- */
  var memory = [];
  function load() {
    try {
      var raw = window.localStorage.getItem(KEY);
      var arr = raw ? JSON.parse(raw) : [];
      if (Array.isArray(arr)) {
        memory = arr.filter(function (r) { return r && typeof r.board === 'string' && typeof r.id === 'string'; });
      }
    } catch (e) { /* storage unavailable: use the in-page copy */ }
    return memory.slice();
  }
  function save(arr) {
    memory = arr.slice();
    try { window.localStorage.setItem(KEY, JSON.stringify(arr)); } catch (e) { /* storage unavailable */ }
    refreshCount();
  }
  function find(arr, board, id) {
    for (var i = 0; i < arr.length; i++) { if (arr[i].board === board && arr[i].id === id) { return i; } }
    return -1;
  }
  function remove(board, id) {
    var arr = load(), i = find(arr, board, id);
    if (i > -1) { arr.splice(i, 1); save(arr); }
  }
  function setNote(board, id, note) {
    var arr = load(), i = find(arr, board, id);
    if (i > -1 && arr[i].note !== note) { arr[i].note = note; save(arr); }
  }
  function clearAll() { save([]); }

  /* ---------- helpers ---------- */
  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) { e.className = cls; }
    if (text != null) { e.textContent = text; }
    return e;
  }

  /* ---------- menu bar ---------- */
  var countLinks = [];
  function refreshCount() {
    var n = memory.length;
    countLinks.forEach(function (a) {
      a.querySelector('b').textContent = String(n);
      a.setAttribute('aria-label', 'Shortlist, ' + n + (n === 1 ? ' concept' : ' concepts') + '. Open the hub');
      a.classList.toggle('is-empty', n === 0);
    });
  }

  function buildBar() {
    var name, prev = null, next = null, i, idx = -1;
    var extra = EXTRA[boardKey];
    for (i = 0; i < BOARDS.length; i++) { if (BOARDS[i].key === boardKey) { idx = i; } }
    if (idx > -1) {
      name = BOARDS[idx].name;
      prev = BOARDS[idx - 1] || null;
      next = BOARDS[idx + 1] || null;
    } else if (extra) {
      name = extra.name;
      prev = extra.prev ? boardByKey(extra.prev) : null;
      next = extra.next ? boardByKey(extra.next) : null;
    } else {
      name = document.title;
    }

    var bar = el('nav', 'hubbar');
    bar.setAttribute('aria-label', 'Logo boards');

    var all = el('a', 'hubbar-all');
    all.href = hubUrl.href;
    var grid = el('span', 'hubbar-grid');
    grid.setAttribute('aria-hidden', 'true');
    all.appendChild(grid);
    all.appendChild(el('span', 'hubbar-long', 'All boards'));
    all.setAttribute('aria-label', 'All boards');
    if (boardKey === 'hub') { all.setAttribute('aria-current', 'page'); }
    bar.appendChild(all);

    function step(b, dir) {
      var a;
      if (b) {
        a = el('a', 'hubbar-step hubbar-' + dir);
        a.href = boardUrl(b);
        a.setAttribute('aria-label', (dir === 'prev' ? 'Previous board, ' : 'Next board, ') + b.name);
      } else {
        a = el('span', 'hubbar-step hubbar-' + dir + ' is-off');
        a.setAttribute('aria-hidden', 'true');
      }
      var arrow = el('span', 'hubbar-arrow', dir === 'prev' ? '‹' : '›');
      arrow.setAttribute('aria-hidden', 'true');
      var lab = el('span', 'hubbar-long', b ? b.name : '');
      if (dir === 'prev') { a.appendChild(arrow); a.appendChild(lab); } else { a.appendChild(lab); a.appendChild(arrow); }
      return a;
    }
    var mid = el('div', 'hubbar-mid');
    mid.appendChild(step(prev, 'prev'));
    mid.appendChild(el('span', 'hubbar-here', name));
    mid.appendChild(step(next, 'next'));
    bar.appendChild(mid);

    var sl = el('a', 'hubbar-count');
    sl.href = hubUrl.href + '#shortlist';
    var star = el('span', 'hubbar-star', '★');
    star.setAttribute('aria-hidden', 'true');
    sl.appendChild(star);
    sl.appendChild(el('b', null, '0'));
    sl.appendChild(el('span', 'hubbar-long', ' shortlisted'));
    countLinks.push(sl);
    bar.appendChild(sl);

    document.body.insertBefore(bar, document.body.firstChild);
    document.documentElement.classList.add('has-hubbar');
    refreshCount();

    /* Keep anchor jumps clear of the menu and the board's own sticky bar. */
    function pad() {
      var h = bar.offsetHeight;
      var cands = document.querySelectorAll('header.top, body > nav.jump');
      for (var k = 0; k < cands.length; k++) {
        if (window.getComputedStyle(cands[k]).position === 'sticky') { h += cands[k].offsetHeight; break; }
      }
      document.documentElement.style.scrollPaddingTop = (h + 8) + 'px';
    }
    pad();
    window.addEventListener('resize', pad);
    /* The browser jumped to the #hash before the menu existed; jump again with the padding in place. */
    if (location.hash.length > 1) {
      var target = null;
      try { target = document.getElementById(decodeURIComponent(location.hash.slice(1))); } catch (e) { target = null; }
      if (target) { target.scrollIntoView(); }
    }
  }

  /* ---------- concept boards: pins, stars, notes ---------- */
  function wireConcepts() {
    var board = boardByKey(boardKey);
    if (!board) { return; }
    var sections = document.querySelectorAll('section.c[id]');
    var items = [];

    Array.prototype.forEach.call(sections, function (sec) {
      var id = sec.id;
      var btn = sec.querySelector('[data-pin], button.pin[data-k]');
      var head = sec.querySelector('.head');
      var h2 = head ? head.querySelector('h2') : null;
      if (!btn || !h2) { return; }
      var name = h2.getAttribute('data-name') ||
        h2.textContent.replace(/^\s*[A-Za-z0-9]+\s*[.·]\s*/, '').trim();
      var link = sec.querySelector('a[data-lockup], a[href$="-lockup.svg"]');
      var file = link ? link.getAttribute('href') : id + '-lockup.svg';

      btn.setAttribute('title', 'Pins here to compare and adds to your shortlist on the hub');

      var star = el('span', 'hub-star');
      var glyph = el('span', 'hub-star-glyph', '★');
      glyph.setAttribute('aria-hidden', 'true');
      star.appendChild(glyph);
      star.appendChild(el('span', 'hub-star-text', 'Shortlisted'));
      star.hidden = true;
      h2.parentNode.insertBefore(star, h2.nextSibling);

      var wrap = el('div', 'hub-note');
      var inputId = 'hub-note-' + board.key + '-' + id;
      var lab = el('label', null, 'Owner notes');
      lab.setAttribute('for', inputId);
      var input = el('input');
      input.type = 'text';
      input.id = inputId;
      input.maxLength = 280;
      input.autocomplete = 'off';
      wrap.appendChild(lab);
      wrap.appendChild(input);
      head.parentNode.insertBefore(wrap, head.nextSibling);

      var item = { id: id, name: name, lockupPath: boardDir(board) + file, btn: btn, star: star, input: input, sec: sec };
      items.push(item);

      var timer;
      input.addEventListener('input', function () {
        clearTimeout(timer);
        timer = setTimeout(function () { setNote(board.key, id, input.value.trim()); }, 250);
      });
      input.addEventListener('change', function () { setNote(board.key, id, input.value.trim()); });
    });
    if (!items.length) { return; }

    function pressed(b) { return b.getAttribute('aria-pressed') === 'true'; }

    function paint() {
      var arr = load();
      items.forEach(function (it) {
        var i = find(arr, board.key, it.id), on = i > -1;
        it.star.hidden = !on;
        it.sec.classList.toggle('is-shortlisted', on);
        it.input.disabled = !on;
        it.input.placeholder = on ? 'Why it made the shortlist' : 'Pin this concept to add a note';
        if (document.activeElement !== it.input) { it.input.value = on ? (arr[i].note || '') : ''; }
      });
    }

    /* The board's own pin state drives the shared shortlist. */
    function syncFromButtons() {
      var arr = load(), changed = false;
      items.forEach(function (it) {
        var i = find(arr, board.key, it.id), on = pressed(it.btn);
        if (on && i === -1) {
          arr.push({ board: board.key, boardName: board.name, id: it.id, name: it.name, lockupPath: it.lockupPath, note: '' });
          changed = true;
        } else if (!on && i > -1) {
          arr.splice(i, 1);
          changed = true;
        }
      });
      if (changed) { save(arr); }
      paint();
    }

    /* The shared shortlist drives the board's pins on load and when another tab changes it. */
    var applying = false;
    var mo = new MutationObserver(function () { if (!applying) { syncFromButtons(); } });
    function syncToButtons() {
      var arr = load();
      applying = true;
      items.forEach(function (it) {
        var want = find(arr, board.key, it.id) > -1;
        if (want !== pressed(it.btn)) { it.btn.click(); }
      });
      mo.takeRecords();
      applying = false;
      paint();
    }

    syncToButtons();
    items.forEach(function (it) { mo.observe(it.btn, { attributes: true, attributeFilter: ['aria-pressed'] }); });

    window.addEventListener('storage', function (e) {
      if (e.key === KEY || e.key === null) { syncToButtons(); }
    });
  }

  function init() {
    load();
    buildBar();
    window.addEventListener('storage', function (e) {
      if (e.key === KEY || e.key === null) { load(); refreshCount(); }
    });
    if (boardKey !== 'hub') { wireConcepts(); }
    document.dispatchEvent(new CustomEvent('logohub:ready'));
  }

  /* Small API for hub.html. */
  window.LogoHub = {
    boards: BOARDS, key: KEY, load: load, save: save, remove: remove, clear: clearAll,
    setNote: setNote, boardByKey: boardByKey, refreshCount: refreshCount
  };

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); } else { init(); }
})();
