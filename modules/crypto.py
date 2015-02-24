import hashlib
import uuid
from string import ascii_uppercase
from random import choice

def get_salt():
    return uuid.uuid4().hex

def get_hash(password, salt):
    password = password.encode('utf-8')
    salt = salt.encode('utf-8')
    return hashlib.sha512(password + salt).hexdigest()

def get_new_sid():
    return str(uuid.uuid4())[:12]