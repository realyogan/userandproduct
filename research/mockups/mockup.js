/* userandproduct mockups: theme toggle, table-of-contents highlight, copy button,
   collapsible anchor, newsletter demo. Plain JS, no dependencies. */
(function () {
  "use strict";
  var KEY = "uap-theme";
  var root = document.documentElement;

  function store(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }
  function systemDark() { return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches; }
  function current() { return root.getAttribute("data-theme") || (systemDark() ? "dark" : "light"); }

  // Pictures with a dark source follow the manual theme as well as the system setting.
  function syncPictures() {
    var t = root.getAttribute("data-theme");
    document.querySelectorAll("source[data-dark]").forEach(function (src) {
      src.media = t === "dark" ? "all" : (t === "light" ? "not all" : "(prefers-color-scheme: dark)");
    });
  }
  syncPictures();

  // Theme toggle: flips between light and dark and remembers the choice.
  document.querySelectorAll("[data-theme-toggle]").forEach(function (btn) {
    function label() { btn.setAttribute("aria-label", current() === "dark" ? "Switch to light theme" : "Switch to dark theme"); }
    label();
    btn.addEventListener("click", function () {
      var next = current() === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      store(next);
      label();
      syncPictures();
    });
  });

  // Table of contents: mark the section being read.
  document.querySelectorAll("[data-toc]").forEach(function (toc) {
    var links = Array.prototype.slice.call(toc.querySelectorAll('a[href^="#"]'));
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); });
    var ticking = false;
    function update() {
      ticking = false;
      var line = window.innerHeight * 0.3, active = -1;
      targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top <= line) { active = i; } });
      links.forEach(function (a, i) {
        if (i === active) { a.setAttribute("aria-current", "true"); } else { a.removeAttribute("aria-current"); }
      });
    }
    window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    window.addEventListener("resize", update);
    update();
  });

  // Copy button for the PRD interview text.
  document.querySelectorAll("[data-copy]").forEach(function (btn) {
    var src = document.getElementById(btn.getAttribute("data-copy"));
    var status = document.getElementById(btn.getAttribute("data-copy-status"));
    btn.addEventListener("click", function () {
      var text = src ? (src.value || src.textContent) : "";
      function done(ok) {
        if (status) { status.textContent = ok ? "Copied. Paste it into a new chat." : "Copy did not work here. Use the text file instead."; }
        setTimeout(function () { if (status) { status.textContent = ""; } }, 4000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(fallback(text)); });
      } else { done(fallback(text)); }
    });
  });
  // Copy-link buttons copy the page address.
  document.querySelectorAll("[data-copy-url]").forEach(function (btn) {
    var status = document.getElementById(btn.getAttribute("data-copy-status"));
    btn.addEventListener("click", function () {
      var url = window.location.href.split("#")[0];
      function done(ok) {
        if (status) { status.textContent = ok ? "Link to the article copied" : "Copy did not work here. Copy the address bar instead."; }
        btn.classList.toggle("is-done", ok);
        clearTimeout(btn._t);
        btn._t = setTimeout(function () { btn.classList.remove("is-done"); if (status) { status.textContent = ""; } }, 2000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(function () { done(true); }, function () { done(fallback(url)); });
      } else { done(fallback(url)); }
    });
  });
  function fallback(text) {
    var ta = document.createElement("textarea");
    ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.top = "-1000px";
    document.body.appendChild(ta); ta.select();
    var ok = false; try { ok = document.execCommand("copy"); } catch (e) {}
    document.body.removeChild(ta); return ok;
  }

  // Mobile anchor ad: appears only after the reader scrolls past the headline, so it never sits over
  // the first screen; collapse and expand; the page padding follows so the end of the page is never covered.
  document.querySelectorAll("[data-anchor]").forEach(function (box) {
    var btn = box.querySelector("[data-anchor-toggle]");
    // data-anchor-until names the first block after the body; the anchor leaves before that block reaches it.
    var until = document.querySelector(box.getAttribute("data-anchor-until") || "null");
    function place() {
      var bodyLeft = until ? until.getBoundingClientRect().top > window.innerHeight + 120 : true;
      box.classList.toggle("is-shown", window.scrollY > 600 && bodyLeft);
    }
    window.addEventListener("scroll", place, { passive: true });
    window.addEventListener("resize", place);
    place();
    if (!btn) { return; }
    btn.addEventListener("click", function () {
      var collapsed = box.classList.toggle("is-collapsed");
      document.body.classList.toggle("anchor-collapsed", collapsed);
      btn.setAttribute("aria-expanded", collapsed ? "false" : "true");
      btn.textContent = collapsed ? "Show ad" : "Hide ad";
    });
  });

  // Newsletter: mockup only, nothing is sent.
  document.querySelectorAll("[data-news]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var s = form.querySelector(".status");
      if (s) { s.textContent = "Mockup: nothing was sent. On the live site this subscribes you to the monthly email."; }
    });
  });

  // ---------- Code blocks ----------
  // Wraps every <pre><code> in a dark card with a bar (dots, language, optional file name, copy button)
  // and highlights sql, javascript, json, bash and html. Language from class="language-x" on code or pre;
  // file name from data-filename on pre; caption from data-caption on pre. Unknown languages stay plain.
  var KW = {
    sql: "select|from|where|and|or|not|as|join|left|right|inner|outer|on|group|by|order|having|limit|offset|insert|into|values|update|set|delete|create|table|index|view|with|distinct|case|when|then|else|end|is|null|in|between|like|filter|count|sum|avg|min|max|union|all|asc|desc|primary|key|references|default",
    javascript: "const|let|var|function|return|if|else|for|while|do|switch|case|break|continue|new|class|extends|import|export|from|default|async|await|try|catch|finally|throw|typeof|instanceof|in|of|this|null|undefined|true|false",
    bash: "if|then|else|elif|fi|for|in|do|done|while|case|esac|function|export|local|return|echo|cd|sudo"
  };
  var RULES = {
    sql: [["com", "--[^\\n]*|/\\*[\\s\\S]*?\\*/"], ["str", "'(?:''|[^'])*'"], ["num", "\\b\\d+(?:\\.\\d+)?\\b"],
          ["kw", "\\b(?:" + KW.sql + ")\\b"], ["fn", "\\b[a-z_]\\w*(?=\\()"]],
    javascript: [["com", "//[^\\n]*|/\\*[\\s\\S]*?\\*/"], ["str", "\"(?:\\\\.|[^\"\\\\])*\"|'(?:\\\\.|[^'\\\\])*'|`(?:\\\\.|[^`\\\\])*`"],
          ["num", "\\b\\d+(?:\\.\\d+)?\\b"], ["kw", "\\b(?:" + KW.javascript + ")\\b"], ["fn", "\\b[A-Za-z_$][\\w$]*(?=\\()"]],
    json: [["key", "\"(?:\\\\.|[^\"\\\\])*\"(?=\\s*:)"], ["str", "\"(?:\\\\.|[^\"\\\\])*\""], ["num", "-?\\b\\d+(?:\\.\\d+)?(?:[eE][+-]?\\d+)?\\b"],
          ["kw", "\\b(?:true|false|null)\\b"]],
    bash: [["com", "(?:^|(?<=\\s))#[^\\n]*"], ["str", "\"(?:\\\\.|[^\"\\\\])*\"|'[^']*'"], ["var", "\\$\\{[^}]+\\}|\\$\\w+"],
          ["kw", "\\b(?:" + KW.bash + ")\\b"], ["fn", "(?:^|(?<=[|;&]\\s*)|(?<=\\n))[A-Za-z_][\\w.-]*"], ["num", "\\b\\d+\\b"]],
    html: [["com", "<!--[\\s\\S]*?-->"], ["tag", "</?[A-Za-z][\\w-]*|/?>"], ["attr", "(?<=\\s)[\\w:-]+(?==)"], ["str", "\"[^\"]*\"|'[^']*'"]]
  };
  var ALIAS = { js: "javascript", sh: "bash", shell: "bash", zsh: "bash", xml: "html", svg: "html" };
  var compiled = {};
  function esc(t) { return t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
  function highlight(text, lang) {
    var rules = RULES[lang];
    if (!rules) { return esc(text); }
    if (!compiled[lang]) {
      var flags = lang === "sql" ? "gim" : "gm";
      compiled[lang] = new RegExp(rules.map(function (r) { return "(" + r[1] + ")"; }).join("|"), flags);
    }
    var re = compiled[lang], out = "", last = 0, m;
    re.lastIndex = 0;
    while ((m = re.exec(text)) !== null) {
      if (m[0] === "") { re.lastIndex++; continue; }
      var g = 1; while (m[g] === undefined) { g++; }
      out += esc(text.slice(last, m.index)) + '<span class="tk-' + rules[g - 1][0] + '">' + esc(m[0]) + "</span>";
      last = m.index + m[0].length;
    }
    return out + esc(text.slice(last));
  }
  var COPY_ICON = '<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><rect x="7" y="7" width="10" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M13 4.5V4a1.5 1.5 0 0 0-1.5-1.5h-7A1.5 1.5 0 0 0 3 4v7a1.5 1.5 0 0 0 1.5 1.5H5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';
  document.querySelectorAll("pre > code").forEach(function (code, i) {
    var pre = code.parentNode;
    if (pre.closest(".codeblock")) { return; }
    var m = ((code.className + " " + pre.className).match(/(?:language|lang)-([\w-]+)/) || [])[1] || "";
    var lang = ALIAS[m] || m;
    var raw = code.textContent.replace(/\n$/, "");
    code.innerHTML = highlight(raw, lang);
    if (pre.hasAttribute("data-lines")) {
      code.innerHTML = code.innerHTML.split("\n").map(function (l) { return '<span class="ln">' + l + "</span>"; }).join("\n");
    }
    var card = document.createElement("div");
    card.className = "codeblock" + (pre.hasAttribute("data-lines") ? " has-lines" : "");
    var id = "code-status-" + i, file = pre.getAttribute("data-filename"), cap = pre.getAttribute("data-caption");
    card.innerHTML = '<div class="codeblock__bar"><span class="codeblock__dots" aria-hidden="true"><i></i><i></i><i></i></span>' +
      (m ? '<span class="codeblock__lang">' + esc(m) + "</span>" : "") +
      (file ? '<span class="codeblock__file">' + esc(file) + "</span>" : "") +
      '<span class="codeblock__status" id="' + id + '" role="status" aria-live="polite"></span>' +
      '<button class="codeblock__copy" type="button" aria-label="Copy code">' + COPY_ICON + "</button></div>";
    pre.parentNode.insertBefore(card, pre);
    card.appendChild(pre);
    if (cap) { var c = document.createElement("p"); c.className = "codeblock__cap"; c.textContent = cap; card.appendChild(c); }
    pre.setAttribute("tabindex", "0");
    pre.setAttribute("aria-label", (m ? m.toUpperCase() + " " : "") + "code" + (file ? ", " + file : ""));
    var btn = card.querySelector(".codeblock__copy"), status = card.querySelector(".codeblock__status");
    btn.addEventListener("click", function () {
      function done(ok) {
        status.textContent = ok ? "Copied" : "Copy did not work here";
        clearTimeout(btn._t);
        btn._t = setTimeout(function () { status.textContent = ""; }, 2000);
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(raw).then(function () { done(true); }, function () { done(fallback(raw)); });
      } else { done(fallback(raw)); }
    });
  });
})();
