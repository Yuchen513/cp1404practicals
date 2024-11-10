from guitar import Guitar

def main():
    guitars = []
    with open('guitars.csv', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    print("Guitars before sorting:")
    for guitar in guitars:
        print(guitar)


    name = input("\nName: ")
    while name !='':
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")


    guitars.sort()

    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    with open('guitars.csv', 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()