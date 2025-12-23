// =====================================================
// Top Navigation Controller (Module-Aware)
// =====================================================

(function () {

  function getEnabledModules() {
    return Array.from(
      document.querySelectorAll(
        '#profile-tab-modules input[name="modules"]:checked'
      )
    ).map(cb => cb.value);
  }

  function applyModuleVisibility() {
    const enabled = getEnabledModules();

    document.querySelectorAll("[data-module]").forEach(el => {
      const key = el.dataset.module;
      el.style.display = enabled.includes(key) ? "" : "none";
    });
  }

  /* -------------------------------
     Overlay open / close
  -------------------------------- */

  document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector("[data-hamburger]");
    const overlay = document.querySelector("[data-nav-overlay]");
    const backdrop = document.querySelector("[data-overlay-backdrop]");

    if (!hamburger || !overlay || !backdrop) return;

    hamburger.addEventListener("click", () => {
      overlay.classList.add("open");
      backdrop.classList.add("open");
    });

    backdrop.addEventListener("click", () => {
      overlay.classList.remove("open");
      backdrop.classList.remove("open");
    });

    document.addEventListener("keydown", e => {
      if (e.key === "Escape") {
        overlay.classList.remove("open");
        backdrop.classList.remove("open");
      }
    });

    applyModuleVisibility();
  });

  /* -------------------------------
     Public refresh hook
  -------------------------------- */

  window.refreshTopNavModules = applyModuleVisibility;

})();
