function validateLogin(event) {
    event.preventDefault(); // Prevent the form from submitting

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email === 'Doctor@123' && password === '12345') {
        window.location.href = 'doctorview.html';
    } else if (email === 'Staff@123' && password === '5678') {
        window.location.href = 'staffview.html';
    } else {
        alert('Invalid credentials');
    }
}