import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode('utf-8')

def create_user(username, password):
    password_hash = hash_password(password)
    user = {'username' : username, 'password' : password_hash}
    return user

def authenticate_user(user, username, password):
    doesMatch = (user['username'] == username
                 and bcrypt.checkpw(password.encode('utf-8'),
                 user['password'].encode('utf-8')))

    return doesMatch


if __name__ == "__main__":
    user = create_user('Cecile', 'pass1234')
    print(authenticate_user(user, 'Cecile', 'pass1234'))
    print(authenticate_user(user, 'Cecile', 'password1234'))