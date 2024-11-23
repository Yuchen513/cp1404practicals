from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    silver_taxi = SilverServiceTaxi("Hummer", 200, 4)

    silver_taxi.start_fare()
    silver_taxi.drive(18)
    fare = silver_taxi.get_fare()
    assert fare == 48.78, f"Expected fare to be 48.78 , got {fare:.2f}"
    print(silver_taxi)


if __name__ == "__main__":
    main()