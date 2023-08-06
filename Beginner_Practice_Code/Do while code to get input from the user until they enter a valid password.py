password = ""

while True:
    password = input("Enter a password: ")

    if len(password) >= 8:
        if password.isalnum():
            break

    print("The password must be at least 8 characters long and contain only letters and numbers.")
