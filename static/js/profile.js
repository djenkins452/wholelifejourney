/* =====================================================
   Whole Life Journey — profile.js (FIXED)
===================================================== */

(function () {
  if (window.__WLJ_PROFILE_JS_LOADED__) return;
  window.__WLJ_PROFILE_JS_LOADED__ = true;

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

  /* -------------------------------
     Modal open / close
  ------------------------------- */

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
     Profile save (CORRECT)
  ------------------------------- */

  document.addEventListener("submit", async e => {
    if (e.target.id !== "profile-form") return;

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
      alert("Failed to save profile.");
      return;
    }

    const displayInput = form.querySelector(
      'input[name="display_name"], input[name$="display_name"]'
    );

    if (displayInput) {
      const newName = displayInput.value.trim();

      /* ONLY update top-right display name */
      document
        .querySelectorAll(".top-nav .muted")
        .forEach(el => el.textContent = newName);
    }

    const msg = document.getElementById("profile-save-message");
    if (msg) {
      msg.style.display = "block";
      setTimeout(() => (msg.style.display = "none"), 2000);
    }
  });

})();
