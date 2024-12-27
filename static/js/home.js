document.getElementById('predict').addEventListener('click', () => {
    // Retrieve values from inputs
    const x = document.getElementById('x').value.trim();
    const y = document.getElementById('y').value.trim();
    const z = document.getElementById('z').value.trim();
    const vx = document.getElementById('vx').value.trim();
    const vy = document.getElementById('vy').value.trim();
    const vz = document.getElementById('vz').value.trim();
  
    // Elements to update
    const videoElement = document.getElementById('result-video');
    const gifElement = document.getElementById('normal-gif');
    const statusElement = document.getElementById('collision-status');
    const errorMessage = document.getElementById('error-message');
  
    // Reset status and error message display
    statusElement.style.display = "none";
    errorMessage.style.display = "none";
  
    // Validate input: Ensure all fields are numbers
    if (
      x === "" || y === "" || z === "" || vx === "" || vy === "" || vz === "" ||
      isNaN(parseFloat(x)) || isNaN(parseFloat(y)) || isNaN(parseFloat(z)) ||
      isNaN(parseFloat(vx)) || isNaN(parseFloat(vy)) || isNaN(parseFloat(vz))
    ) {
      errorMessage.textContent = "Please enter valid coordinates and velocities!";
      errorMessage.style.display = "block";
      return;
    }
  
    // Parse inputs as numbers
    const xNum = parseFloat(x);
    const yNum = parseFloat(y);
    const zNum = parseFloat(z);
    const vxNum = parseFloat(vx);
    const vyNum = parseFloat(vy);
    const vzNum = parseFloat(vz);
  
    // Logic to determine collision
    const collisionOccurred = Math.abs(xNum + yNum + zNum) < 100 && Math.abs(vxNum + vyNum + vzNum) > 10;
  
    // Set the appropriate video source
    if (collisionOccurred) {
      videoElement.src = "Collision.mp4";
      statusElement.textContent = "Collision occurred!";
      statusElement.style.color = "red";
    } else {
      videoElement.src = "No Collision.mp4";
      statusElement.textContent = "No collision occurred!";
      statusElement.style.color = "green";
    }
  
    // Hide the GIF and show the video
    gifElement.style.display = "none";
    videoElement.style.display = "block";
    videoElement.play();
  
    // Show collision status
    statusElement.style.display = "block";
  });
  
  // Ensure GIF is displayed on page reload
  window.addEventListener('load', () => {
    const videoElement = document.getElementById('result-video');
    const gifElement = document.getElementById('normal-gif');
    const statusElement = document.getElementById('collision-status');
    const errorMessage = document.getElementById('error-message');
  
    // Reset to show GIF and hide video, status, and error message
    videoElement.style.display = "none";
    gifElement.style.display = "block";
    statusElement.style.display = "none";
    errorMessage.style.display = "none";
  });
  