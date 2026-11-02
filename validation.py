"""Validation functions: check the user input before saving it."""


def is_valid_name(name):
    name = name.strip()
    return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)


def is_valid_email(email):
    email = email.strip()
    if " " in email or email.count("@") != 1:
        return False
    user, domain = email.split("@")
    return len(user) > 0 and "." in domain and not domain.startswith(".") and not domain.endswith(".")


def is_valid_age(age):
    return 16 <= age <= 60


def is_valid_grade(grade):
    return 0 <= grade <= 100


def read_int(message):
    """Keep asking until the user types a whole number."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Error: please enter a number.")


def read_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: please enter a number.")
