import base64
import json
from cryptography.fernet import Fernet


def generate_key(password):
    # Generate a random key
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_password = cipher.encrypt(password.encode())
    print(key, encrypted_password)
    return key, encrypted_password
def decrypt_password(key, encrypted_password):
    cipher = Fernet(key)
    password = cipher.decrypt(encrypted_password).decode()
    return password

def encode_password(encrypted_password):
    return base64.b64encode(encrypted_password).decode()

def decode_password(encoded_password):
    return base64.b64decode(encoded_password.encode())

def create_user_account(user, master_p):
    # create a file name based on the username
    filename = f"{user}.json"

    # Check if the user already exists
    try:
        with open(filename, 'r') as file:
            print(f"User '{user}' already exists.")
            return
    # If not, create a new account for the user
    except FileNotFoundError:
        # Generate a random key for encryption
        key, encrypted_password = generate_key(master_p)

        # user's credentials
        user_vault = {
            "user": user,
            "master_p": encode_password(encrypted_password),
            "vault": []

        }

        with open(filename, 'w') as file:
            json.dump(user_vault, file, indent=2)

        print(f"User account for '{user}' has been created")


def check_user_acc(user, master_p):
    filename = f"{user}.json"

    try:
        with open(filename, 'r') as file:
            user_vault = json.load(file)
            key = generate_key(decrypt_password(decode_password(user_vault["master_p"]), master_p))[0]
            decrypted_password = decrypt_password(key, user_vault["master_p"])
            if decrypted_password == master_p:
                return True
            else:
                return False

    except FileNotFoundError:
        return False


## Idea Dump
'''
user_vault = {
        "user": user,

        "vault": [
            "username":username,
            "password": password,
            "website": website,
        ]
    }
'''

'''
create_user_file(user, master_p, username=None, password=None, website=None):
'''



'''
    try:
        with open(filename, 'r') as file:
            user_vault = json.load(file)
            key = generate_key(password)[0]
            encrypted_password = generate_key(password)[1]
            website_creds = {
                "website": website,
                "encrypted_password": encrypted_password,
            }
            user_vault.setdefault("credentials", []).append(website_creds)

        with open(filename, 'w') as file:
            json.dump(user_vault, file)

        print(f"Account for {username} has been created. Your file name is {filename}.")
    except FileNotFoundError:
        key, encrypted_password = generate_key(password)
        user_vault = {
            "username": username,
            "credentials": initial_credentials if initial_credentials else [
                {
                    "website": website,
                    "encrypted_password": encrypted_password
                }
            ]
        }
        with open(filename, 'w') as file:
            json.dump(user_vault, file)
        print(f"Account for {username} has been created. Your file name is {filename}.")
    '''