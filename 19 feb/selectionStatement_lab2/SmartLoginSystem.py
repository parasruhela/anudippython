correct_username = "admin"
correct_password = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    # Username validation
    if username != correct_username:
        print("Invalid Username!")
    # Password validation
    elif password != correct_password:
        print("Invalid Password!")
    else:
        print("Login Successful!")
        break

    attempts += 1
    print(f"Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Account Locked! Too many failed attempts.")