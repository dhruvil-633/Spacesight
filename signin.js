document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('signinForm');
    
    form.addEventListener('submit', (event) => {
        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        if (username === '' || password === '') {
            alert('Both fields are required!');
            event.preventDefault(); // Prevent form submission
        } else {
            // Optionally, add more validation logic here
            // Example: Validate email format for username
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(username)) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Prevent form submission
            }
        }
    });
});
