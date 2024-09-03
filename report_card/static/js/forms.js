function validateForm() {
    var form = document.getElementById("form");
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var text = document.getElementById("text"); 
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    // Perform email validation
    if (email.match(emailPattern)){
        form.classList.add("valid");
        form.classList.remove("invalid");
        text.innerHTML = "Your email address is valid";
        text.style.color = "#00ff00";
    }
    else if (email === ""){
        form.classList.remove("valid");
        form.classList.add("invalid");
        text.innerHTML = "Please enter an email";
        text.style.color = "#ff0000";
        return false; // Stop form submission if email is empty
    }
    else{
        form.classList.remove("valid");
        form.classList.add("invalid");
        text.innerHTML = "Please enter a valid email";
        text.style.color = "#ff0000";
        return false; // Stop form submission if email is invalid
    }
    
    // Perform password validation
    if (password.length < 8) {
        form.classList.remove("valid");
        form.classList.add("invalid");
        text.innerHTML = "Password must be at least 8 characters long";
        text.style.color = "#ff0000";
        return false; // Stop form submission if password is too short
    }
    
    // Additional validation logic can be added here

    return true; // Allow form submission if all validations pass
}
