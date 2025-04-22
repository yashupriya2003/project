document.getElementById('resetPasswordBtn').addEventListener('click', function() {
    const usn = document.getElementById('usn').value;
    const email = document.getElementById('email').value;
    const newPassword = document.getElementById('new_password').value;

    // Validate inputs
    if (!usn || !email || !newPassword) {
        alert("Please fill in all fields.");
        return;
    }

    // Prepare the data to be sent to the server
    const data = {
        usn: usn,
        email: email,
        new_password: newPassword
    };

    // Make AJAX request to reset password
    fetch('/reset-password', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Password reset successfully!');
            window.location.href = '/student_login';  // Redirect to login page
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while resetting your password.');
    });
});
