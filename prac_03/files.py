open('data.txt', 'w')

# 1
name = input("What's your name? ")
file = open('name.txt', 'w')
file.write(name)
file.close()

# 2
file = open('name.txt', 'r')
read_name = file.read()
print(f"Hi {read_name}!")
file.close()

# 3
with open('numbers.txt', 'w') as file:
    file.write("17\n42\n400")
with open('numbers.txt','r') as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
print(num1 + num2)

# 4
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total = total + int(line)
print(total)