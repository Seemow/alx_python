def validate_password(password):
    test = True
    if len(str(password)) < 8:
        test = False 

    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_uppercase is False or has_lowercase is False or has_digit is False:
        test = False
    
    if " " in password:
        test = False

    return test