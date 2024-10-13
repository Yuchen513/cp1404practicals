"in a shop"

while True:
    try:
        num_items = int(input("Number of items: "))
        if num_items < 0:
            print("Invalid number of items!")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

total_price = 0
for _ in range(num_items):
    while True:
        try:
            item_price = float(input("Price of item: "))
            total_price += item_price
            break
        except ValueError:
            print("Invalid input. Please enter a valid price.")

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {num_items} items is ${total_price:.2f}")