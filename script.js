document.addEventListener("DOMContentLoaded", () => {
  const usernameInput = document.getElementById("username");
  const status = document.getElementById("username-status");

  if (usernameInput) {
    usernameInput.addEventListener("input", () => {
      const username = usernameInput.value;
      if (username.length > 2) {
        fetch(`/check_username/${username}`)
          .then(res => res.json())
          .then(data => {
            if (data.available) {
              status.textContent = "✅";
              status.style.color = "green";
            } else {
              status.textContent = "❌";
              status.style.color = "red";
            }
          });
      } else {
        status.textContent = "";
      }
    });
  }
});
