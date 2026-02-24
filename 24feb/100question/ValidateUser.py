username = input().strip()
password = input().strip()

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")