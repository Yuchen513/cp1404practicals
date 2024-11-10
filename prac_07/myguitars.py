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

    guitars.sort()

    print("\nGuitars after sorting by year (oldest to newest):")
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()