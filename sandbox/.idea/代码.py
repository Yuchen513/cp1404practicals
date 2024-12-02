
import csv
import random


def load_places(filename):
    """Load places from a CSV file into a list."""
    places = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                row[2] = int(row[2])  # Convert priority to integer
                places.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with an empty list.")
    return places


def save_places(filename, places):
    """Save places to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow(place)


def display_places(places, visited_status, unvisited_status):
    """Display all places with their details and visit status."""
    if not places:
        print("No places to display.")
        return
    places.sort(key=lambda p: (p[3] == visited_status, p[2]))  # Sort by visit status and priority
    for i, place in enumerate(places, 1):
        mark = '*' if place[3] == unvisited_status else ' '
        print(f"{mark}{i}. {place[0]:<10} in {place[1]:<15} Priority: {place[2]}")
    unvisited_count = sum(1 for place in places if place[3] == unvisited_status)
    print(f"\n{len(places)} places tracked. You still want to visit {unvisited_count} places.\n")


def recommend_place(places, unvisited_status):
    """Recommend a random unvisited place."""
    unvisited_places = [place for place in places if place[3] == unvisited_status]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print(f"Not sure where to visit next? How about... {place[0]} in {place[1]}?")
    else:
        print("No places left to visit!")


def add_place(places, unvisited_status):
    """Add a new place to the list with input validation."""
    name = input("Name: ").strip()
    while not name:
        print("Input cannot be blank")
        name = input("Name: ").strip()

    country = input("Country: ").strip()
    while not country:
        print("Input cannot be blank")
        country = input("Country: ").strip()

    try:
        priority = int(input("Priority: "))
        while priority <= 0:
            print("Number must be > 0")
            priority = int(input("Priority: "))
    except ValueError:
        print("Invalid input; enter a valid number.")
        return  # Stop adding if invalid input

    places.append([name, country, priority, unvisited_status])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def mark_place_visited(places, visited_status, unvisited_status):
    """Mark an unvisited place as visited."""
    unvisited_places = [place for place in places if place[3] == unvisited_status]
    if not unvisited_places:
        print("No unvisited places.")
        return
    display_places(places, visited_status, unvisited_status)
    try:
        choice = int(input("Enter the number of a place to mark as visited: "))
        if 0 < choice <= len(places):
            selected_place = places[choice - 1]
            if selected_place[3] == visited_status:
                print(f"You have already visited {selected_place[0]}")
            else:
                selected_place[3] = visited_status
                print(f"{selected_place[0]} in {selected_place[1]} visited!")
        else:
            print(f"The number you entered is not in the list range (1-{len(places)}).")
    except ValueError:
        print("Invalid input; please enter a valid number.")


def display_menu():
    print(
        "Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit")


def main():
    filename = 'places.csv'
    visited_status = 'v'
    unvisited_status = 'n'
    places = load_places(filename)

    print("Travel Tracker 1.0 - by [Your Name]")
    print(f"{len(places)} places loaded from {filename}")

    while True:
        display_menu()
        choice = input(">>> ").upper()
        if choice == 'D':
            display_places(places, visited_status, unvisited_status)
        elif choice == 'R':
            recommend_place(places, unvisited_status)
        elif choice == 'A':
            add_place(places, unvisited_status)
        elif choice == 'M':
            mark_place_visited(places, visited_status, unvisited_status)
        elif choice == 'Q':
            save_places(filename, places)
            print(f"{len(places)} places saved to {filename}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()

