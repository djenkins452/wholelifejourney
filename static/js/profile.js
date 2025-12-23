/* =====================================================
   Whole Life Journey — profile.js (FINAL)
===================================================== */

(function () {
  if (window.__WLJ_PROFILE_JS_LOADED__) return;
  window.__WLJ_PROFILE_JS_LOADED__ = true;

  /* ================================
     CSRF Helper
  ================================ */

  function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(";").shift();
    return null;
  }

  function getCsrfToken(form) {
    const input = form.querySelector("input[name='csrfmiddlewaretoken']");
    return input ? input.value : getCookie("csrftoken");
  }

  function norm(v) {
    return (v || "").toString().trim().toLowerCase();
  }

  /* ================================
     Modal Open / Close
  ================================ */

  window.openProfileModal = function () {
    document.getElementById("profileModal")?.classList.remove("hidden");
  };

  window.closeProfileModal = function () {
    document.getElementById("profileModal")?.classList.add("hidden");
  };

  document.addEventListener("keydown", e => {
    if (e.key === "Escape") window.closeProfileModal();
  });

  /* ================================
     Profile Tabs
  ================================ */

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
    if (panel) panel.classList.add("active");
  });

  /* ================================
     Profile Save (Display Name Sync)
  ================================ */

  document.addEventListener("submit", async e => {
    if (e.target.id !== "profile-form") return;

    e.preventDefault();

    const form = e.target;
    const csrfToken = getCsrfToken(form);

    const response = await fetch(form.action || window.location.href, {
      method: "POST",
      body: new FormData(form),
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrfToken
      }
    });

    if (!response.ok) {
      alert("Failed to save profile.");
      return;
    }

    /* ----------------------------------------
       Update top-right display name live
    ---------------------------------------- */

    const displayInput = form.querySelector(
      'input[name="display_name"], input[name$="display_name"]'
    );

    if (displayInput) {
      const newName = displayInput.value.trim();
      if (newName) {
        const topbarName = document.querySelector(".topbar .muted");
        if (topbarName) {
          topbarName.textContent = newName;
        }
      }
    }

    const msg = document.getElementById("profile-save-message");
    if (msg) {
      msg.style.display = "block";
      setTimeout(() => (msg.style.display = "none"), 2000);
    }
  });

  /* ================================
     Modules Save + Sidebar Update
  ================================ */

  document.addEventListener("submit", async e => {
    if (e.target.id !== "profile-modules-form") return;

    e.preventDefault();

    const form = e.target;
    const csrfToken = getCsrfToken(form);

    const response = await fetch(form.action, {
      method: "POST",
      body: new FormData(form),
      credentials: "same-origin",
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrfToken
      }
    });

    if (!response.ok) {
      alert("Failed to save modules.");
      return;
    }

    /* ----------------------------------------
       SAFE SIDEBAR SYNC (ONLY HIDE IF EXPLICIT)
    ---------------------------------------- */

    const checkboxMap = {};
    form.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      checkboxMap[norm(cb.value)] = cb.checked;
    });

    document.querySelectorAll(".sidebar [data-module]").forEach(link => {
      const key = norm(link.dataset.module);

      if (key in checkboxMap) {
        if (checkboxMap[key]) {
          link.hidden = false;
          link.style.display = "block";
        } else {
          link.hidden = true;
          link.style.display = "none";
        }
      }
    });

    const msg = document.getElementById("modules-save-message");
    if (msg) {
      msg.style.display = "block";
      setTimeout(() => (msg.style.display = "none"), 2000);
    }
  });
})();
