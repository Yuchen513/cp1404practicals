def main():
 min_length = 8
 password = get_password()
 while len(password) < min_length:
    print(f"The password should be at least {min_length} characters long.")
    password = input("Please enter again: ")
 print_star(password)


def print_star(password):
    print("*" * len(password))


def get_password():
    password = input("Please enter your password: ")
    return password


main()