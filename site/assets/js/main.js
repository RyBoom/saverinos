/* Savarino's Market concept: small, dependency free. */
(function () {
  "use strict";
  var root = document.documentElement;
  var body = document.body;
  root.classList.remove("no-js");
  root.classList.add("js");

  /* ---------- Hours, in Central time ---------- */
  // 0 = Sunday. Open and close in 24h hours.
  var HOURS = [
    [10, 15], // Sunday
    [10, 16], // Monday
    [10, 16], // Tuesday
    [10, 17], // Wednesday
    [10, 17], // Thursday
    [10, 17], // Friday
    [10, 17]  // Saturday
  ];
  var DAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

  // Review aid: ?now=2026-10-10T16:30 reads that as Central time.
  function chicagoNow() {
    var param = new URLSearchParams(location.search).get("now");
    if (param) {
      var m = param.match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})/);
      if (m) {
        var d = new Date(Date.UTC(+m[1], +m[2] - 1, +m[3]));
        return { day: d.getUTCDay(), minutes: +m[4] * 60 + +m[5] };
      }
    }
    var parts = new Intl.DateTimeFormat("en-US", {
      timeZone: "America/Chicago", weekday: "short", hour: "numeric", minute: "numeric", hour12: false
    }).formatToParts(new Date());
    var get = function (t) { return parts.filter(function (p) { return p.type === t; })[0].value; };
    var day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(get("weekday"));
    return { day: day, minutes: (+get("hour") % 24) * 60 + +get("minute") };
  }

  function clock(h) { return h > 12 ? h - 12 : h; }

  function statusFor(now) {
    var h = HOURS[now.day];
    var open = h[0] * 60, close = h[1] * 60;
    if (now.minutes >= open && now.minutes < close) {
      var left = close - now.minutes;
      var text = left <= 60 ? "Open until " + clock(h[1]) + ". Closing soon." : "Open now until " + clock(h[1]);
      return { open: true, text: text };
    }
    if (now.minutes < open) return { open: false, text: "Closed. Opens at " + clock(h[0]) + " today" };
    return { open: false, text: "Closed. Back at " + clock(HOURS[(now.day + 1) % 7][0]) + " tomorrow" };
  }

  function paintStatus() {
    var now = chicagoNow();
    var st = statusFor(now);
    document.querySelectorAll("[data-status]").forEach(function (el) {
      el.dataset.open = String(st.open);
      var t = el.querySelector("[data-status-text]");
      if (t) t.textContent = st.text;
    });
    document.querySelectorAll("[data-hours] tr[data-day]").forEach(function (tr) {
      tr.classList.toggle("today", +tr.dataset.day === now.day);
    });
  }
  paintStatus();
  setInterval(paintStatus, 60000);

  /* ---------- Header: logo takes over once the hero logo has scrolled away ---------- */
  var heroLogo = document.querySelector("[data-hero-logo]");
  var pageEl = document.querySelector(".home") || body;
  if (heroLogo && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      pageEl.classList.toggle("past-hero", !entries[0].isIntersecting);
    }, { rootMargin: "-72px 0px 0px 0px" }).observe(heroLogo);
  } else if (heroLogo) {
    pageEl.classList.add("past-hero");
  }

  /* ---------- Mobile nav ---------- */
  var toggle = document.querySelector(".hdr-toggle");
  var panel = document.getElementById("hdr-panel");
  if (toggle && panel) {
    toggle.addEventListener("click", function () {
      var open = panel.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    panel.addEventListener("click", function (e) {
      if (e.target.closest("a")) { panel.classList.remove("open"); toggle.setAttribute("aria-expanded", "false"); }
    });
  }

  /* ---------- Designer notes toggle ---------- */
  var notesBtn = document.querySelector("[data-notes-toggle]");
  function setNotes(on) {
    body.classList.toggle("notes-off", !on);
    if (notesBtn) {
      notesBtn.textContent = on ? "Hide designer notes" : "Show designer notes";
      notesBtn.setAttribute("aria-pressed", String(!on));
    }
    try { localStorage.setItem("sv-notes", on ? "on" : "off"); } catch (e) { /* storage may be blocked */ }
  }
  var saved = null;
  try { saved = localStorage.getItem("sv-notes"); } catch (e) { /* ignore */ }
  setNotes(saved !== "off");
  if (notesBtn) notesBtn.addEventListener("click", function () { setNotes(body.classList.contains("notes-off")); });

  /* ---------- Menu: scroll spy for the category nav ---------- */
  var catNav = document.querySelector(".cat-nav");
  if (catNav && "IntersectionObserver" in window) {
    var links = Array.prototype.slice.call(catNav.querySelectorAll("a"));
    var byId = {};
    links.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
    var current = null;
    var setCurrent = function (id) {
      if (id === current || !byId[id]) return;
      current = id;
      links.forEach(function (a) { a.removeAttribute("aria-current"); });
      byId[id].setAttribute("aria-current", "true");
      var ul = byId[id].closest("ul");
      if (ul && ul.scrollWidth > ul.clientWidth) {
        var a = byId[id];
        ul.scrollTo({ left: a.offsetLeft - (ul.clientWidth - a.offsetWidth) / 2, behavior: "smooth" });
      }
    };
    var sections = Array.prototype.slice.call(document.querySelectorAll(".board"));
    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { visible[e.target.id] = e.isIntersecting; });
      var found = false;
      for (var i = 0; i < sections.length; i++) { if (visible[sections[i].id]) { setCurrent(sections[i].id); found = true; break; } }
      // Above the first board there is nothing to highlight: clear it and rewind the strip.
      if (!found && sections[0].getBoundingClientRect().top > window.innerHeight * 0.35) {
        current = null;
        links.forEach(function (a) { a.removeAttribute("aria-current"); });
        var strip = catNav.querySelector("ul");
        if (strip) strip.scrollTo({ left: 0, behavior: "smooth" });
      }
    }, { rootMargin: "-20% 0px -65% 0px" });
    sections.forEach(function (s) { io.observe(s); });
    if (location.hash && byId[location.hash.slice(1)]) setCurrent(location.hash.slice(1));
  }

  /* ---------- Open the wholesale form from a hash ---------- */
  function openWholesale() {
    var d = document.getElementById("wholesale-form");
    if (d && (location.hash === "#wholesale-form")) d.open = true;
  }
  openWholesale();
  window.addEventListener("hashchange", openWholesale);

  /* ---------- Forms (concept: validates, does not send) ---------- */
  document.querySelectorAll("form[data-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (el) {
        var err = el.parentElement.querySelector(".err");
        var bad = !el.value.trim();
        el.setAttribute("aria-invalid", String(bad));
        if (err) err.textContent = bad ? el.dataset.error || "Please fill this in." : "";
        if (bad) ok = false;
      });
      if (!ok) { var first = form.querySelector('[aria-invalid="true"]'); if (first) first.focus(); return; }
      var done = form.querySelector(".form-ok");
      form.querySelectorAll(".f, .f-row, .btn, .form-note").forEach(function (n) { n.hidden = true; });
      if (done) { done.hidden = false; done.setAttribute("tabindex", "-1"); done.focus(); }
    });
  });

  /* ---------- The delight: fill the cannoli ---------- */
  document.querySelectorAll("[data-stage]").forEach(function (stage) {
    var btn = stage.querySelector("[data-fill]");
    var pic = stage.querySelector(".cannoli");
    var msg = stage.querySelector("[data-stage-status]");
    function set(filled) {
      stage.classList.toggle("filled", filled);
      btn.textContent = filled ? "Start over" : "Fill it";
      btn.setAttribute("aria-pressed", String(filled));
      pic.setAttribute("aria-pressed", String(filled));
      msg.textContent = filled ? "Filled to order. Now come get one." : "Empty shell. Go ahead.";
    }
    function flip() { set(!stage.classList.contains("filled")); }
    btn.addEventListener("click", flip);
    pic.addEventListener("click", flip);
    set(false);
  });
})();
