document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    
    form.addEventListener('submit', (event) => {
        const x = document.getElementById('x-coordinate').value.trim();
        const y = document.getElementById('y-coordinate').value.trim();
        const z = document.getElementById('z-coordinate').value.trim();
        const velocityX = document.getElementById('velocity-x').value.trim();
        const velocityY = document.getElementById('velocity-y').value.trim();
        const velocityZ = document.getElementById('velocity-z').value.trim();

        let valid = true;
        let errorMsg = '';

        // Check if all fields are filled
        if (x === '' || y === '' || z === '' || velocityX === '' || velocityY === '' || velocityZ === '') {
            errorMsg += 'All fields are required.\n';
            valid = false;
        }

        // Check if inputs are numbers (allowing negative and decimal numbers)
        const numberPattern = /^-?\d*\.?\d+$/;

        if (!numberPattern.test(x) || !numberPattern.test(y) || !numberPattern.test(z) ||
            !numberPattern.test(velocityX) || !numberPattern.test(velocityY) || !numberPattern.test(velocityZ)) {
            errorMsg += 'Coordinates and velocities must be valid numbers (positive or negative, including decimal values).\n';
            valid = false;
        }

        // If not valid, show alert and prevent form submission
        if (!valid) {
            alert(errorMsg);
            event.preventDefault(); // Prevent form submission
        }
    });
});
