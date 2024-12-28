document.getElementById('prediction-form').addEventListener('submit', async function (event) {
  event.preventDefault();

  // Get form data
  const x = document.getElementById('x').value;
  const y = document.getElementById('y').value;
  const z = document.getElementById('z').value;
  const vx = document.getElementById('vx').value;
  const vy = document.getElementById('vy').value;
  const vz = document.getElementById('vz').value;

  // Send data to the backend
  const response = await fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ x, y, z, vx, vy, vz })
  });
  const result = await response.json();

  // Replace form-container content with the appropriate video
  const formContainer = document.querySelector('.form-container');
  formContainer.innerHTML = `
    <video autoplay muted playsinline>
      <source src="/static/img/${result.result === 1 ? 'collision' : 'no_collision'}.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>
  `;

  // Show result after the video finishes
  const video = formContainer.querySelector('video');
  video.addEventListener('ended', () => {
    formContainer.innerHTML = `
      <h2 style="text-align: center;">
        ${result.result === 1 ? 'Collision will occur!' : 'No collision detected.'}
      </h2>
    `;
  });
});