// =====================================================
// Profile Modal Controller (AUTHORITATIVE)
// =====================================================

(function () {

  /* -------------------------------
     Modal open / close (REQUIRED GLOBALS)
  -------------------------------- */

  window.openProfileModal = function () {
    const modal = document.getElementById("profileModal");
    if (modal) modal.classList.remove("hidden");
  };

  window.closeProfileModal = function () {
    const modal = document.getElementById("profileModal");
    if (modal) modal.classList.add("hidden");
  };

  document.addEventListener("keydown", e => {
    if (e.key === "Escape") {
      window.closeProfileModal();
    }
  });

  /* -------------------------------
     Tabs
  -------------------------------- */

  document.querySelectorAll(".profile-tab").forEach(tab => {
    tab.addEventListener("click", e => {
      e.preventDefault();

      document
        .querySelectorAll(".profile-tab")
        .forEach(t => t.classList.remove("active"));

      document
        .querySelectorAll(".profile-tab-panel")
        .forEach(p => p.classList.remove("active"));

      tab.classList.add("active");

      const panelId = "profile-tab-" + tab.dataset.tab;
      document.getElementById(panelId)?.classList.add("active");
    });
  });

  /* -------------------------------
     Profile Save (AJAX)
  -------------------------------- */

  const profileForm = document.getElementById("profile-form");
  if (profileForm) {
    profileForm.addEventListener("submit", e => {
      e.preventDefault();

      fetch(profileForm.action, {
        method: "POST",
        body: new FormData(profileForm),
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      })
        .then(r => r.json())
        .then(data => {
          if (data.status === "ok") {
            const msg = document.getElementById("profile-save-message");
            if (msg) msg.style.display = "block";

            // Update display name live
            const nameInput = profileForm.querySelector("input[name='display_name']");
            const display = document.querySelector(".profile-trigger .muted");
            if (nameInput && display) {
              display.textContent = nameInput.value;
            }
          }
        });
    });
  }

  /* -------------------------------
     Modules Save (AJAX)
  -------------------------------- */

  const modulesForm = document.getElementById("profile-modules-form");
  if (modulesForm) {
    modulesForm.addEventListener("submit", e => {
      e.preventDefault();

      fetch(modulesForm.action, {
        method: "POST",
        body: new FormData(modulesForm),
        headers: {
          "X-Requested-With": "XMLHttpRequest",
        },
      })
        .then(r => r.json())
        .then(data => {
          if (data.status === "ok") {
            const msg = document.getElementById("modules-save-message");
            if (msg) msg.style.display = "block";

            // 🔑 Recompute enabled modules and update nav live
            const enabledKeys = Array.from(
              modulesForm.querySelectorAll("input[name='modules']:checked")
            ).map(cb => cb.value);

            if (window.updateEnabledModules) {
              window.updateEnabledModules(enabledKeys);
            }
          }
        });
    });
  }

})();
