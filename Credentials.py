import json
import bcrypt
import os


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password, salt


def save(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)


"""def add(filename, data):
    with open(filename, 'a+') as file:
        json.dump(data, file, indent=2)
"""


def load(filename):
    with open(filename, 'r') as file:
        file_data = json.load(file)
    return file_data


def check_password(master_p, stored_hash, salt):
    hashed_input = bcrypt.hashpw(master_p.encode('utf-8'), salt)
    return hashed_input == stored_hash


def create_user_account(user, master_p, email):
    # create a file name based on the username
    filename = f"{user}.json"

    hashed_password, salt = hash_password(master_p)

    # Check if the user already exists
    try:
        with open(filename, 'r') as file:
            print(f"User '{user}' already exists.")
            return
    # If not, create a new account for the user
    except FileNotFoundError:

        # user's account(vault)

        user_vault = {
            "user": user,
            "master_p": hashed_password.decode('utf-8'),
            "salt": salt.decode('utf-8'),
            "email": email,

            "vault": []

        }

        save(filename, user_vault)

        print(f"User account for '{user}' has been created")


def add_user_credentials(user, username, password, website):
    filename = f"{user}_passwords.json"

    if not os.path.exists(filename):
        data = []
    else:

        try:
            with open(filename, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = []

    credentials = {
        "username": username,
        "password": password,
        "website": website
    }
    data.append(credentials)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Credentials for '{user}' has been added.")


def login(user, master_p):
    filename = f"{user}.json"
    userdata = load(filename)

    try:
        with open(filename, 'r') as file:

            if check_password(master_p, userdata['master_p'].encode('utf-8'), userdata['salt'].encode('utf-8')):

                print(f"Login successful for user '{user}'.")
                return True
            else:
                print("Login failed.")
                return None

    except FileNotFoundError:
        print("File does not exist. Create a new one!")
        return None


def show_user_credentials(user):
    filename = f"{user}_passwords.json"

    try:
        with open(filename, 'r') as file:
            show_data = json.load(file)
            print("\nYour Credentials...\n")
            for x in show_data:
                print("Username:", x['username'], "Password:", x['password'], "Website:", x['website'])
                print("\n")
            print('\n')
    except FileNotFoundError:
        print("\n You do not have any passwords saved!")

    return x
