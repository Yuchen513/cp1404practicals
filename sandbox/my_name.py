"""
CP1404/CP5632 Assignment 1 - Travel Tracker

Student Name: [Your Name]
GitHub Repository Link: [Your Repository Link]
"""

import random

# 定义表示访问状态的常量
VISITED = 'v'
UNVISITED = 'n'
def main():
    file_path = "places.csv"
    places = load_places(file_path)
    print(f"Travel Tracker 1.0 - by {__name__} {len(places)} places loaded from {file_path}")
    menu = {
        "D": display_places,
        "R": lambda: print(recommend_place(places) if recommend_place(places) is not None else "No places left to visit!"),
        "A": add_place,
        "M": mark_visited,
        "Q": lambda: save_places(places, file_path)
    }
    while True:
        print("Menu: D - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit")
        choice = input(">>> ").upper()
        if choice in menu:
            menu[choice](places)
            if choice == "Q":
                break
        else:
            print("Invalid menu choice")

def load_places(file_path):
    """从CSV文件加载地点数据"""
    places = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            name, country, priority, visited = line.strip().split(',')
            places.append([name, country, int(priority), visited])
    return places

def save_places(places, file_path):
    """将地点数据保存到CSV文件"""
    with open(file_path, 'w') as file:
        for place in places:
            file.write(','.join([place[0], place[1], str(place[2]), place[3]]) + '\n')

def display_places(places):
    """显示地点列表"""
    longest_name = max(len(place[0]) for place in places)
    longest_country = max(len(place[1]) for place in places)
    print("Places:")
    for i, place in enumerate(places, start=1):
        visited_status = ""
        if place[3] == UNVISITED:
            visited_status = "*"
        print(f"{visited_status}{i}. {place[0]:<{longest_name}} in {place[1]:<{longest_country}} {place[2]}")
    total_places = len(places)
    unvisited_places = sum(1 for place in places if place[3] == UNVISITED)
    print(f"{total_places} places tracked. You still want to visit {unvisited_places} places.")

def recommend_place(places):
    """推荐一个未访问的地点"""
    unvisited = [place for place in places if place[3] == UNVISITED]
    if unvisited:
        return random.choice(unvisited)
    return None

def add_place(places):
    """添加一个新地点"""
    name = input("Name: ")
    while not name:
        print("Name: Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while not country:
        print("Country: Input can not be blank")
        country = input("Country: ")
    priority = input("Priority: ")
    while True:
        try:
            priority = int(priority)
            if priority <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input; enter a valid number")
            priority = input("Priority: ")
    places.append([name, country, priority, UNVISITED])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")

def mark_visited(places):
    """标记一个地点为已访问"""
    display_places(places)
    if all(place[3] == VISITED for place in places):
        print("No unvisited places")
        return
    while True:
        try:
            place_number = int(input("Enter the number of a place to mark as visited >>> "))
            if place_number <= 0 or place_number > len(places):
                raise ValueError
                break
            selected_place = places[place_number - 1]
            if selected_place[3] == VISITED:
                print("You have already visited this place")
            else:
                selected_place[3] = VISITED
                print(f"{selected_place[0]} in {selected_place[1]} visited!")
                break
        except ValueError:
            print("Invalid input; enter a valid number")



if __name__ == "__main__":
    main()