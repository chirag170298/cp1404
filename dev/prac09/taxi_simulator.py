from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    current_taxi = None
    print("(q)uit, (c)hoose taxi, (d)rive")
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
                print("Bill to date: ${:.2f}".format(bill_to_date))
            except IndexError:
                print("Invalid taxi choice")
                print("Bill to date: ${:.2f}".format(bill_to_date))
                current_taxi = None

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                fare = current_taxi.get_fare()
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                bill_to_date += fare
                print("Bill to date: ${:.2f}".format(bill_to_date))

        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(bill_to_date))

        print("(q)uit, (c)hoose taxi, (d)rive")
        choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


if __name__ == '__main__':
    main()
