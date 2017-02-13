import re

def is_valid_username(username):
    """A username is valid if it fulfills the following conditions:
    - Contains at least 8 characters and at most 12 characters
    - Only contains letters from A to Z, a to z and digits from 0 to 9
    - Contains at least one digit
    - Must start with a capital letter

    Args:
        username (str): A username string
    Returns:
        bool: True if username is valid, False otherwise
    """
    if 8 <= len(username) <= 12 \
        and re.match('^[A-Z][A-Za-z]+\d+', username) is not None:
        return True

    return False

def is_valid_us_zip_code(zip):
    """A valid fulfills one of the following conditions:
    - Consists of 5 digits
        e.g. 55555
    - Consists of 5 digits followed by a dash (-) followed by 4 digits
        e.g. 55555-5555

    Args:
        zip (str): A zip code string
    Returns:
        bool: True if zip is a valid US zip code, False otherwise
    """
    if re.match('\d{5}|\d{5}-\d{4}', zip) is not None:
        return True

    return False
