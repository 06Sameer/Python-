# Simple Login System

users = {
    "admin": "1234",
    "sameer": "pass"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Credentials")

# Output:
# Login Successful / Invalid Credentials
