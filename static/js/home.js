document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('prediction-form').addEventListener('submit', async function (event) {
    event.preventDefault(); // Prevent form from reloading the page

    // Get form data
    const x = document.getElementById('x').value;
    const y = document.getElementById('y').value;
    const z = document.getElementById('z').value;
    const vx = document.getElementById('vx').value;
    const vy = document.getElementById('vy').value;
    const vz = document.getElementById('vz').value;

    try {
      // Send data to the backend
      const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ x_sim: x, y_sim: y, z_sim: z, Vx_sim: vx, Vy_sim: vy, Vz_sim: vz })
      });

      const result = await response.json();

      // Update the form container content
      const formContainer = document.querySelector('.form-container');
      formContainer.innerHTML = `
        <div class="result-container">
          <h2 style="text-align: center; color: #ADD8E6;">
            ${result.result === "Collision will happen" ? 'Collision will occur!' : 'No collision detected.'}
          </h2>
        </div>
        <div class="video-container">
          <video autoplay muted playsinline>
            <source src="/static/img/${result.prediction === 1 ? 'collision' : 'no_collision'}.mp4" type="video/mp4">
            Your browser does not support the video tag.
          </video>
        </div>
      `;
    } catch (error) {
      console.error('Error during prediction:', error);
    }
  });
});
