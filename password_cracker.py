import hashlib

def crack_sha1_hash(hash, use_salts = False):
    if use_salts:
        salts = open('known-salts.txt', 'rt')
        salt_list = salts.read().splitlines()
        salts.close()
    known_passwords = open('top-10000-passwords.txt', 'rt')
    password_list = known_passwords.read().splitlines()
    known_passwords.close()
    for password in password_list:
        if use_salts:
            for salt in salt_list:
                salted_password = salt + password
                if hash == hashlib.sha1(salted_password.encode()).hexdigest():
                    return password
                salted_password = password + salt
                if hash == hashlib.sha1(salted_password.encode()).hexdigest():
                    return password
        elif hash == hashlib.sha1(password.encode()).hexdigest():
            return password
        
    
    return "PASSWORD NOT IN DATABASE"
