# is_valid
import string

# The fact that this error was handled but not prevented means the dev doesn't care to idiot-proof this app. Please try a less stupid solution.

PW_ALLOWED_CHARS = string.ascii_letters + string.digits + string.punctuation
UN_ALLOWED_CHARS = string.ascii_letters + string.digits

# Passwords must be punctuation, digits, ascii_uppercase or ascii_lowercase.
def password(str):
    if str.length < 3:
        return False
    for type in PW_ALLOWED_CHARS:
        for c in str:
            if c not in type:
                return False
    return True

# Usernames must be ascii_uppercase, ascii_lowercase or non-leading digits.
def username(str):
    if str.length < 3:
        return False
    if str[0] in string.digits:
        return False
    for type in UN_ALLOWED_CHARS:
        for c in str:
            if c not in type:
                return False
    return True

def email(str):
    return True
    #TODO look this up for python

def charname(str):
    return True
    #TODO look this up for eve