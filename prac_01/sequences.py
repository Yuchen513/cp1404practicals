

x = int(input("starting number (x): "))
y = int(input("ending number (y): "))

while True:
    print("\nMenu:")
    print("1. Show the even numbers from x to y")
    print("2. Show the odd numbers from x to y")
    print("3. Show the squares of the numbers from x to y")
    print("4. Exit the program")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        for num in range(x, y + 1):
            if num % 2 == 0:
                print(num, end=' ')
    elif choice == 2:
        for num in range(x, y + 1):
            if num % 2 == 1:
                print(num, end=' ')
    elif choice == 3:
        for num in range(x, y + 1):
            print(num * num, end=' ')
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice.")