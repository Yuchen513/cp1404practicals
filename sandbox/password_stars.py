"""
CP1404 Assignment 1 - Travel Tracker
Name:Yuchen Liu
Date started:25/10/2024
GitHub URL:https://github.com/cp1404-students/a1-Yuchen513.git
"""

import random
import csv

def main():
    filename = "places.csv "
    print(f"Travel Tracker 1.0 - by Yuchen \n3 places loaded from  places.csv")
    visited_status = 'v'
    unvisited_status = 'n'
    places = load_places(filename)
    print("Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit")
    while True:
        choice = input(">>> ").upper()
        if choice == 'D':
            display_places(places, visited_status, unvisited_status)
        elif choice == 'R':
            recommend_place(places, unvisited_status)
        elif choice == 'A':
            add_place(places,unvisited_status)
        elif choice == 'M':
            mark_place_visited(places, visited_status, unvisited_status)
        elif choice == 'Q':
            save_places(places, filename)
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")
            print("Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit")

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
    print(f"{len(places)} places tracked. You still want to visit {unvisited_count} places.")

def recommend_place(places,unvisited_status):
    #Recommend a random unvisited place.
    unvisited_places = []
    for place in places:
        if place[3] == unvisited_status:
            unvisited_places.append(place)
    if unvisited_places:
        random_place = random.choice(unvisited_places)
        print(f"Not sure where to visit next? \nHow about... {random_place[0]} in {random_place[1]}?")
        print("Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit")
    else:
        print("No places left to visit!")

def add_place(places,unvisited_status):
    """Add a new place with user input."""
    name = input("Name: ").strip()
    while not name:
        print("Input can not be blank")
        name = input("Name: ").strip()
    country = input("Country: ").strip()
    while not country:
        print("Input can not be blank")
        country = input("Country: ").strip()
    priority = False
    while not priority:
        try:
            priority = int(input("Priority: "))
            if priority <= 0:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")
    places.append([name, country, priority, unvisited_status])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")
    print("Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit")

def display_menu():
    print("Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit")

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


def save_places(filename, places):
    """Save places to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow(place)



if __name__ == '__main__':
    main()
