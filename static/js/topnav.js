// =====================================================
// Top Navigation Controller (Module-Aware — STABLE)
// =====================================================

(function () {

  function getEnabledModuleKeysFromJSON() {
    const script = document.getElementById("enabled-modules");
    if (!script) return [];
    try {
      return JSON.parse(script.textContent || "[]");
    } catch {
      return [];
    }
  }

  function applyModuleVisibility() {
    const enabled = getEnabledModuleKeysFromJSON();

    document.querySelectorAll("[data-module]").forEach(el => {
      const key = el.dataset.module;
      el.style.display = enabled.includes(key) ? "" : "none";
    });

    const healthSubs = document.querySelector("[data-health-subitems]");
    if (healthSubs) {
      healthSubs.hidden = !enabled.includes("health");
    }

    const topHealthSubs = document.querySelector("[data-health-top-subitems]");
    if (topHealthSubs) {
      topHealthSubs.hidden = true; // ALWAYS CLOSED ON LOAD
    }
  }

  function setupHealthToggle() {
    const topToggle = document.querySelector("[data-health-top-toggle]");
    const topSubs = document.querySelector("[data-health-top-subitems]");
    const chevron = topToggle ? topToggle.querySelector(".chevron") : null;

    if (!topToggle || !topSubs) return;

    topToggle.addEventListener("click", e => {
      e.preventDefault();

      const isOpen = !topSubs.hasAttribute("hidden");

      // Toggle ONLY on Health click
      if (isOpen) {
        topSubs.setAttribute("hidden", "");
        if (chevron) chevron.textContent = "▸";
      } else {
        topSubs.removeAttribute("hidden");
        if (chevron) chevron.textContent = "▾";
      }
    });
  }

  /* -------------------------------
     Public update hook
  -------------------------------- */

  window.updateEnabledModules = function (keys) {
    const script = document.getElementById("enabled-modules");
    if (!script) return;

    script.textContent = JSON.stringify(keys || []);
    applyModuleVisibility();
  };

  window.refreshTopNavModules = applyModuleVisibility;

  /* -------------------------------
     Overlay open / close (unchanged)
  -------------------------------- */

  document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector("[data-hamburger]");
    const overlay = document.querySelector("[data-nav-overlay]");
    const backdrop = document.querySelector("[data-overlay-backdrop]");

    

    if (hamburger && overlay && backdrop) {
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
    }

    applyModuleVisibility();
    setupHealthToggle();
  });

})();
