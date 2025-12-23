/* =====================================================
   Whole Life Journey — profile.js
===================================================== */

(function () {
  if (window.__WLJ_PROFILE_JS_LOADED__) return;
  window.__WLJ_PROFILE_JS_LOADED__ = true;

  function getCsrfToken(form) {
    const input = form.querySelector("input[name='csrfmiddlewaretoken']");
    return input ? input.value : null;
  }

  /* -------------------------------
     Modal open / close
  -------------------------------- */

  window.openProfileModal = function () {
    document.getElementById("profileModal")?.classList.remove("hidden");
  };

  window.closeProfileModal = function () {
    document.getElementById("profileModal")?.classList.add("hidden");
  };

  document.addEventListener("keydown", e => {
    if (e.key === "Escape") closeProfileModal();
  });

  /* -------------------------------
     Profile modal tabs
  -------------------------------- */

  document.addEventListener("click", e => {
    const tab = e.target.closest(".profile-tab");
    if (!tab) return;

    e.preventDefault();

    const modal = document.getElementById("profileModal");
    if (!modal) return;

    modal.querySelectorAll(".profile-tab").forEach(t => t.classList.remove("active"));
    modal.querySelectorAll(".profile-tab-panel").forEach(p => p.classList.remove("active"));

    tab.classList.add("active");
    const panel = modal.querySelector(`#profile-tab-${tab.dataset.tab}`);
    panel?.classList.add("active");
  });

  /* -------------------------------
     Profile save (display name)
  -------------------------------- */

  document.addEventListener("submit", async e => {
    if (e.target.id !== "profile-form") return;

    e.preventDefault();
    const form = e.target;

    const response = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { "X-Requested-With": "XMLHttpRequest" },
      credentials: "same-origin"
    });

    if (!response.ok) return alert("Failed to save profile.");

    const input = form.querySelector('input[name$="display_name"]');
    if (input) {
      document.querySelectorAll(".top-nav .muted")
        .forEach(el => el.textContent = input.value.trim());
    }

    const msg = document.getElementById("profile-save-message");
    msg && (msg.style.display = "block");
    setTimeout(() => msg && (msg.style.display = "none"), 2000);
  });

  /* -------------------------------
     Modules save (AJAX)
  -------------------------------- */

  document.addEventListener("submit", async e => {
    if (e.target.id !== "profile-modules-form") return;

    e.preventDefault();
    const form = e.target;

    const response = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      headers: { "X-Requested-With": "XMLHttpRequest" },
      credentials: "same-origin"
    });

    if (!response.ok) return alert("Failed to save modules.");

    const msg = document.getElementById("modules-save-message");
    msg && (msg.style.display = "block");
    setTimeout(() => msg && (msg.style.display = "none"), 2000);

    if (window.refreshTopNavModules) {
      window.refreshTopNavModules();
    }
  });

})();
