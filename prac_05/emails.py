"""
CP5632 Practical 5
Estimate: 20 minutes
Actual:   34 minutes
"""


def main():
    emails_names = {}
    email = input("Email: ")
    while email != "":
        name = name_function(email)
        response = input(f"Is your name {name}? (Y/n) ")
        if response.lower() == 'n':
            name = input("Name: ")
        emails_names[email] = name
        email = input("Email: ")
    for email, name in emails_names.items():
        print(f"{name} ({email})")


def name_function(email):
    parts = email.split('@')[0].split('.')
    name = " ".join([part.title() for part in parts])
    return name


main()