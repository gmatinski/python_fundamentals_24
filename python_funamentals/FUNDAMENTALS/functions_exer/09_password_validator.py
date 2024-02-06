def is_length_valid(password):
    return 6 <= len(password) <= 10


def is_alphanumeric(password):
    return password.isalnum()


def has_at_least_two_digits(password):
    digit_count = sum(char.isdigit() for char in password)
    return digit_count >= 2


def is_valid_password(password):
    if is_length_valid(password) and is_alphanumeric(password) and has_at_least_two_digits(password):
        print("Password is valid")
    else:
        if not is_length_valid(password):
            print("Password must be between 6 and 10 characters")
        if not is_alphanumeric(password):
            print("Password must consist only of letters and digits")
        if not has_at_least_two_digits(password):
            print("Password must have at least 2 digits")


password_input = input()
is_valid_password(password_input)
