from modules.crypto import *
from modules.connect import c

def add_session(uid):
    sid = get_new_sid()
    c.execute("INSERT INTO Sessions (sid, uid) VALUES(:sid, :uid)", {"sid":sid, "uid":uid})
    return sid

def drop_session(sid):
    c.execute("DELETE FROM Sessions WHERE sid = :sid", {"sid":sid})
    return sid

def verify_session(sid):
    c.execute("SELECT uid FROM Sessions WHERE sid = :sid", {"sid":sid})
    res = c.fetchone()
    if res is not None:
        return res[0]
    else:
        return None

def verify_user(username, password):
    c.execute("SELECT uid,hash,salt FROM Users WHERE username = :username", {"username":username})
    res = c.fetchone()
    if res is not None:
        if res[1] == get_hash(password, res[2]):
            return res[0]
    else:
        return None

def add_user(username, password, charname, email):
    # Verification
    if not is_valid.username(username):
        return False
    if not is_valid.password(password):
        return False
    if not is_valid.email(email):
        return False
    if not is_valid.charname(charname):
        return False

    salt = get_salt()
    data = {
    "uid"      : get_new_uid(),
    "username" : username,
    "hash"     : get_hash(password,salt),
    "salt"     : salt,
    "pid"      : 1,
    "charname" : charname,
    "email"    : email
    }
    c.execute("""INSERT INTO Users (uid, username, hash, salt, pid, charname, email)
                             VALUES(:uid, :username, :hash, :salt, :pid, :charname, :email)""", data)
    return True