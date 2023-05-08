"""Client code to test SilverServiceTaxi class"""

from silver_service_taxi import SilverServiceTaxi


def main():
    service_taxi = SilverServiceTaxi("Hummer", 100, 2)
    service_taxi.drive(18)
    print(service_taxi)
    print(f"Total fare is ${service_taxi.get_fare():.2f}")


main()
