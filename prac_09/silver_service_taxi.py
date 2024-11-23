from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        base_fare = super().get_fare()
        return round(base_fare + self.flagfall, 2)

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, plus flagfall of ${self.flagfall}"