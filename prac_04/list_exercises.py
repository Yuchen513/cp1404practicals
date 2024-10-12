def main():
    numbers = []
    for _ in range(5):
        num = int(input("Number: "))
        numbers.append(num)

    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))

main()

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

input_username = input("Please enter your username: ")
if input_username in usernames:
    print("Access granted")
else:
    print("Access denied")