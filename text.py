def print_user(secret):
    print(f"Name: {get_name(secret)}")
    print(f"Password: {secret['password']}")

def get_name(secret):
    return secret["name"]

def set_name(secret, val):
    secret["name"] = val

if __name__ == "__main__":
    print_user({'name':'user', 'password':'password'})