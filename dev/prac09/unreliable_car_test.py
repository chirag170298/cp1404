"""Client code to test UnreliableCar class"""

from unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Prius 1", 100, 55)
    my_car.drive(40)
    print(f"{my_car.name} drove {my_car._odometer}")


main()
