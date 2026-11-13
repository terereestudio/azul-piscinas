/* Remanso Piscinas — interacciones mínimas (sin dependencias, compatible con CSP estricta) */
"use strict";
(() => {
  /* 1. Email armado con JS (evita scraping del texto plano) */
  document.querySelectorAll("[data-mail-user]").forEach((el) => {
    const user = el.getAttribute("data-mail-user") || "";
    const domain = el.getAttribute("data-mail-domain") || "";
    if (!user || !domain) return;
    const address = user + "@" + domain;
    const label = el.querySelector("[data-mail-label]");
    if (label) label.textContent = address;
    if (el.tagName === "A") el.setAttribute("href", "mailto:" + encodeURIComponent(user) + "@" + encodeURIComponent(domain));
  });

  /* 2. Año del copyright */
  document.querySelectorAll("[data-year]").forEach((el) => { el.textContent = String(new Date().getFullYear()); });

  /* 3. Formulario: trampa de tiempo + honeypot + bloqueo de doble envío */
  const form = document.getElementById("form-contacto");
  if (form) {
    const loadedAt = Date.now();
    const msg = form.querySelector(".form-msg");
    const button = form.querySelector("button[type='submit']");
    form.addEventListener("submit", (event) => {
      const honeypot = form.querySelector("input[name='bot-field']");
      const tooFast = Date.now() - loadedAt < 3000;
      if ((honeypot && honeypot.value !== "") || tooFast) {
        event.preventDefault();
        if (msg) msg.textContent = "No pudimos enviar el formulario. Esperá unos segundos y probá de nuevo.";
        return;
      }
      if (!form.checkValidity()) return;
      if (button) { button.disabled = true; button.textContent = "Enviando…"; }
    });
  }
})();
