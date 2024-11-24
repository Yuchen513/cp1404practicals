from prac_09.unreliable_car import UnreliableCar


def main():
    #Testing
    my_car = UnreliableCar("My car", 50, 40)
    print(f"{my_car.name} : {my_car.drive(5)}km")
    print(my_car)

    my_car2 = UnreliableCar("My car2", 70, 70)
    print(f"{my_car2.name} : {my_car2.drive(10)}km")
    print(my_car2)

    my_car3 = UnreliableCar("My car3", 60, 20)
    print(f"{my_car3.name} : {my_car3.drive(15)}km")
    print(my_car3)




main()