s = {
    'username': "phillip.gachnag@fhnw.ch",
    'password': "mysupersecretpassword"
}

def p_secret(secret):
    print(f"Name: {secret['username']}")
    print(f"Password: {secret['password']}")

p_secret(s)