min_length = 8
password = input("Please enter your password: ")
while len(password) < min_length:
    print(f"The password should be at least {min_length} characters long.")
    password = input("Please enter again: ")
print("*" * len(password))
