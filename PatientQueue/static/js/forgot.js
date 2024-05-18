function validatePassword(event) {
    event.preventDefault(); // Prevent the form from submitting

    const email = document.getElementById('email').value;
   
    var password;

    if (email === 'Doctor@123' && email==='Staff@123') {
        password=document.getElementById('password')
        alert("Password changed successfully!!!")
    }
    else{
        alert("Invalid User Id!!!")
    }
    }
