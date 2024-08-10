document.querySelector('.predict-btn').addEventListener('click', function(event) {
    event.preventDefault();  // Prevent the default form submission behavior

    // Collect form data
    const x_sim = document.getElementById('x-coordinate').value;
    const y_sim = document.getElementById('y-coordinate').value;
    const z_sim = document.getElementById('z-coordinate').value;
    const Vx_sim = document.getElementById('velocity-x').value;
    const Vy_sim = document.getElementById('velocity-y').value;
    const Vz_sim = document.getElementById('velocity-z').value;

    // Ensure all fields are filled before making the request
    if (x_sim && y_sim && z_sim && Vx_sim && Vy_sim && Vz_sim) {
        // Send data to the Flask backend
        fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'x_sim': x_sim,
                'y_sim': y_sim,
                'z_sim': z_sim,
                'Vx_sim': Vx_sim,
                'Vy_sim': Vy_sim,
                'Vz_sim': Vz_sim
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display the prediction result
            const resultArea = document.querySelector('.result-area');
            resultArea.innerHTML = `<h2>${data.result}</h2>`;
        })
        .catch(error => {
            console.error('Error:', error);
            // Display an error message in the result area
            const resultArea = document.querySelector('.result-area');
            resultArea.innerHTML = `<h2>Error occurred: ${error.message}</h2>`;
        });
    } else {
        // Handle missing fields
        alert("Please fill in all the fields before predicting.");
    }
});