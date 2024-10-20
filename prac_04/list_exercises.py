def main():
    numbers = []
    count = 1

    while count > 0 :
        num = float (input(f"Number{count}: "))
        if num < 0:
            break
        numbers.append(num)
        count = count + 1

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