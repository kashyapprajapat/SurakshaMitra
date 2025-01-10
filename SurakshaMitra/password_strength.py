def check_strength(password):
    """
    Evaluates the strength of a given password and categorizes it as:
    Very Weak, Weak, Average, Strong, or Very Strong.
    """
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Include at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Include at least one lowercase letter.")

    # Check for special characters
    if any(char in "!@#$%^&*()-_+=" for char in password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    # Determine the strength category based on the score
    if score == 0:
        strength = "Very Weak"
    elif score == 1:
        strength = "Weak"
    elif score == 2:
        strength = "Average"
    elif score == 3:
        strength = "Strong"
    elif score >= 4:
        strength = "Very Strong"

    # Provide detailed feedback if the password is not very strong
    if score < 4:
        return f"{strength}: {' '.join(feedback)}"
    else:
        return f"{strength}: Your password is secure."
    


