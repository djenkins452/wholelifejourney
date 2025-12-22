function openProfileModal() {
  document.getElementById("profileModal").classList.remove("hidden");
}

function closeProfileModal() {
  document.getElementById("profileModal").classList.add("hidden");
}

document.addEventListener("keydown", e => {
  if (e.key === "Escape") closeProfileModal();
});

/* ----------------------------------------
   Profile Tabs
---------------------------------------- */
document.addEventListener("click", e => {
  if (!e.target.classList.contains("profile-tab")) return;

  e.preventDefault();

  document.querySelectorAll(".profile-tab").forEach(tab =>
    tab.classList.remove("active")
  );

  document.querySelectorAll(".profile-tab-panel").forEach(panel =>
    panel.classList.remove("active")
  );

  e.target.classList.add("active");
  const tabName = e.target.dataset.tab;
  document.getElementById(`profile-tab-${tabName}`).classList.add("active");
});

/* ----------------------------------------
   Profile Form (Timezone AJAX submit)
---------------------------------------- */
document.addEventListener("submit", async e => {
  if (e.target.id !== "profile-form") return;

  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

const csrfToken = form.querySelector(
  "input[name='csrfmiddlewaretoken']"
).value;

const response = await fetch("/profile/", {
  method: "POST",
  body: formData,
  headers: {
    "X-Requested-With": "XMLHttpRequest",
    "X-CSRFToken": csrfToken
  }
});


  if (response.ok) {
    const msg = document.getElementById("profile-save-message");
    if (msg) {
      msg.style.display = "block";
      setTimeout(() => {
        msg.style.display = "none";
      }, 2000);
    }
  } else {
    alert("Failed to save profile.");
  }
});

/* ----------------------------------------
   Modules Form (AJAX submit)
---------------------------------------- */
document.addEventListener("submit", async e => {
  if (e.target.id !== "profile-modules-form") return;

  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

  const response = await fetch(form.action, {
    method: "POST",
    body: formData,
    headers: {
      "X-Requested-With": "XMLHttpRequest"
    }
  });

  if (response.ok) {
    const msg = document.getElementById("modules-save-message");
    if (msg) {
      msg.style.display = "block";
      setTimeout(() => {
        msg.style.display = "none";
      }, 2000);
    }
  } else {
    alert("Failed to save modules.");
  }
});
