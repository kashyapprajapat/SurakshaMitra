# SurakshaMitra

SurakshaMitra 🔐 is your security companion for managing passwords 🔑 and validating email 📨 addresses.

## Features ☕

- Check password strength 💪🏻
- Generate strong passwords ♨️
- Validate email addresses 📧

## Total Downloaders
![screencapture-pepy-tech-projects-surakshamitra-2025-01-28-19_43_04](https://github.com/user-attachments/assets/0e30c1f9-d428-432c-813f-b03e2b75418f)


## Installation

Install SurakshaMitra using pip:

```bash
pip install SurakshaMitra
```

## Usage


## 1. Check Password Strength
To check the strength of a password, use the check_strength() function:

```bash
from SurakshaMitra.password_strength import check_strength

password = "YourPassword123!"
result = check_strength(password)
print(result)
```
### output
This will output the strength of the password as one of the following categories:

-Weak

-Average

-Medium

-Strong

-Very Strong




## 2. Generate Strong Passwords
To generate a strong password, use the generate_password() function:

```bash
from SurakshaMitra.password_generator import generate_password

password = generate_password(length=12)  # Specify the length of the password
print("Generated Password:", password)
```

### output
This will generate a random, strong password with a mix of characters, numbers, and special symbols.


## 3. Validate Email Address
To validate an email address, use the validate_email() function:

from SurakshaMitra.email_validator import validate_email

```bash
email = "example@example.com"
is_valid = validate_email(email)
if is_valid:
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")
```

☕
For any issues or questions, feel free to raise an issue in the GitHub repository.





### Explanation:
- **Password Strength**: This demonstrates how to use the `check_strength()` function to evaluate the strength of a password.
- **Password Generator**: Shows how to use the `generate_password()` function to create a strong password.
- **Email Validator**: Guides the user to use `validate_email()` to check if an email address is formatted correctly.

### Total downloads 
[click to see](https://pepy.tech/projects/surakshamitra?timeRange=threeMonths&category=version&includeCIDownloads=true&granularity=daily&viewType=table&versions=1.1.0%2C1.0.0)

![WhatsApp Image 2025-01-28 at 3 54 47 PM](https://github.com/user-attachments/assets/6b31789f-ce8b-48a7-92b1-b90ebaf46906)

