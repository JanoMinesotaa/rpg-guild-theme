/* THE LONG NIGHT · landing sezonu - skrypt wspólny czterech sekcji.
 * ---------------------------------------------------------------------------
 * Robi mniej niż prototyp, i to jest celowe. W prototypie skrypt liczył też,
 * które akty są jeszcze zamknięte, bo strona przełączała je w locie przez
 * ?act=. W motywie akt jedzie z ustawienia sekcji, więc klasa `is-locked`
 * i zwinięcie przycisków są już w wyrenderowanym HTML-u - nie ma czego liczyć
 * po stronie przeglądarki i nie ma mignięcia odsłoniętej treści przed startem
 * skryptu.
 *
 * Zostały dwie rzeczy:
 *   1. wejście sekcji (jedyny ruch wjazdowy na stronie),
 *   2. drobna ergonomia pola e-mail - formularz jest NATYWNY (`form 'customer'`),
 *      więc skrypt go NIE przechwytuje. Zapis leci do Shopify, skąd bierze go
 *      Edrone; gdyby skrypt padł, formularz dalej działa.
 *
 * Projekt nie ma biblioteki animacji, więc strona też nie ma.
 */
(function () {
  "use strict";

  /* Każda z czterech sekcji wstawia ten plik - wykonujemy się tylko raz. */
  if (window.__lnLp) return;
  window.__lnLp = true;

  /* Bezpiecznik zmiany aktu (27.10.2026). Akt liczy serwer z daty, ale Shopify
   * mógł podać stronę z cache wyrenderowaną przed północą. Jeśli kalendarz mówi
   * już o wyższym akcie niż HTML, przeładowujemy RAZ z parametrem `ln`, który
   * omija cache. Parametr w adresie = nie próbujemy drugi raz (zero pętli). */
  (function () {
    var root = document.querySelector(".ln-lp[data-act-auto]");
    if (!root || /[?&]ln=/.test(location.search)) return;
    var now = Date.now(), want = 1;
    if (now >= Date.UTC(2026, 10, 30, 23)) want = 3;      /* 1.12 00:00 CET */
    else if (now >= Date.UTC(2026, 9, 31, 23)) want = 2;  /* 1.11 00:00 CET */
    if (want > (parseInt(root.getAttribute("data-act"), 10) || 1)) {
      location.replace(location.pathname + (location.search ? location.search + "&" : "?") + "ln=" + want + location.hash);
    }
  })();

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");

  function wejscie(root) {
    var items = (root || document).querySelectorAll(".ln-reveal:not(.is-in)");
    if (!items.length) return;

    function pokazWszystko() {
      for (var i = 0; i < items.length; i++) items[i].classList.add("is-in");
    }

    if (reduce.matches || !("IntersectionObserver" in window)) {
      pokazWszystko();
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add("is-in");
        io.unobserve(e.target);
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });

    for (var j = 0; j < items.length; j++) io.observe(items[j]);

    /* Bezpiecznik: gdyby obserwator nie zdążył (szybki scroll, wolne obrazy),
       po dwóch sekundach i tak pokazujemy wszystko. Nigdy pusta strona. */
    window.setTimeout(pokazWszystko, 2000);
  }

  /* Formularz: TYLKO podpowiedź przy oczywistej literówce w adresie i stan
     "wysyłam" na przycisku. Żadnego preventDefault - submit ma dojść do
     Shopify. Walidację właściwą i tak robi serwer, a komunikaty renderuje
     Liquid z `form.errors` / `form.posted_successfully?`. */
  function formularz(root) {
    var form = (root || document).querySelector(".ln-form");
    if (!form || form.dataset.lnReady === "1") return;
    form.dataset.lnReady = "1";

    var input = form.querySelector("input[type='email']");
    var button = form.querySelector("button[type='submit']");
    var msg = form.querySelector(".ln-form__msg");
    if (!input) return;

    var spoczynek = msg ? msg.textContent : "";
    var napisPrzycisku = button ? button.textContent : "";

    function powiedz(tekst, stan) {
      if (!msg) return;
      msg.textContent = tekst;
      if (stan) msg.setAttribute("data-state", stan);
      else msg.removeAttribute("data-state");
    }

    input.addEventListener("input", function () {
      input.removeAttribute("aria-invalid");
      if (msg && msg.getAttribute("data-state") === "error") powiedz(spoczynek, null);
    });

    form.addEventListener("submit", function (ev) {
      var v = input.value.trim();
      if (!v || v.indexOf("@") < 1 || v.indexOf(".", v.indexOf("@")) < 0) {
        ev.preventDefault();
        input.setAttribute("aria-invalid", "true");
        powiedz(input.getAttribute("data-blad") || "Check that address and try again.", "error");
        input.focus();
        return;
      }
      if (button) {
        button.setAttribute("data-state", "loading");
        button.textContent = button.getAttribute("data-napis-wysylam") || napisPrzycisku;
      }
    });
  }

  function start(root) { wejscie(root); formularz(root); }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () { start(document); });
  } else {
    start(document);
  }

  /* Edytor motywu przerenderowuje pojedynczą sekcję bez przeładowania strony -
     bez tego nowo wstawiony blok zostałby niewidoczny (opacity:0). */
  document.addEventListener("shopify:section:load", function (e) { start(e.target); });
})();
