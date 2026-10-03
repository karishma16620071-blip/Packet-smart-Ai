document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".planner-form").forEach(form => {
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const result = document.getElementById("result");
      const button = form.querySelector("button");
      button.disabled = true;
      button.textContent = "Generating...";

      try {
        const response = await fetch(form.dataset.endpoint, {
          method: "POST",
          body: new FormData(form)
        });
        const data = await response.json();
        result.textContent = data.result || data.detail || "No result.";
        result.classList.remove("hidden");
      } catch (error) {
        result.textContent = "Something went wrong. Please check the server and try again.";
        result.classList.remove("hidden");
      } finally {
        button.disabled = false;
        button.textContent = "Generate Plan";
      }
    });
  });
});
