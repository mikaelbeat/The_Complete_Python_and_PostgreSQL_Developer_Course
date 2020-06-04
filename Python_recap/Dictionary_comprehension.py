
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "rolf1234"),
    (2, "Jose", "longpassword"),
    (3, "username", "12345")
]

username_mapping = {user[1]: user for user in users}

username_input = "Bob"
password_input = "password"

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Credentials are correct!")
else:
    print("Your details are incorrect!")