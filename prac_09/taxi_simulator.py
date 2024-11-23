from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu_choice = ""
    while menu_choice != "q":
        display_menu()
        menu_choice = input(">>> ").lower()
        if menu_choice == "c":
            current_taxi = choose_taxi(taxis)
            if current_taxi:
                print(f"You chose {current_taxi}")
        elif menu_choice == "d":
            total_bill += drive_taxi(current_taxi)
        elif menu_choice != "q":
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_menu():
    print("q)uit, c)hoose taxi, d)rive")


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    display_taxis(taxis)
    taxi_choice = input("Choose taxi: ")
    if taxi_choice.isdigit():
        taxi_choice = int(taxi_choice)
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
    else:
        print("Invalid input. Please enter a number.")
    return None


def drive_taxi(current_taxi):
    if current_taxi:
        distance = input("Drive how far? ")
        if distance.isdigit():
            distance = int(distance)
            current_taxi.start_fare()
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            return trip_cost
        else:
            print("Invalid input. Please enter a number.")
    else:
        print("You need to choose a taxi before you can drive.")
    return 0


if __name__ == "__main__":
    main()