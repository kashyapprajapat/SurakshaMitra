import random
import string

def generate_password(length=12):
    """
    Generates a strong password of specified length.
    """
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    characters = string.ascii_letters + string.digits + "!@#$%^&*()-_+="
    return ''.join(random.choice(characters) for _ in range(length))

