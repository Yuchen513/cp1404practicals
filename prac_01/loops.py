for i in range(1, 21, 2):
    print(i, end=' ')
print()


for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("input a number："))
for _ in range(n):
    print('*', end='')
print()

n = int(input("input a number："))
for i in range(1, n + 1):
    for _ in range(i):
        print('*', end='')
    print()