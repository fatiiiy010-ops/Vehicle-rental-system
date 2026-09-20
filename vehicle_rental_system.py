# Parent class
class Vehicle:
    def __init__(self, vehicle_id, brand, rent_per_day ):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.rent_per_day = rent_per_day
        self.is_available = True

    def display_info(self):
        print(f'Vehicle id : {self.vehicle_id}')
        print(f'Brand : {self.brand}')
        print(f'Rent per day : {self.rent_per_day}')
        print(f'Availability : {self.is_available}')

    def rent_vehicle(self):
        if self.is_available:
            self.is_available = False
            print('Vehicle rented successfully.')
        else:
            print('This vehicle is already rented. Please choose another vehicle.')

    def return_vehicle(self):
        if not self.is_available:
            self.is_available = True
            print('Vehicle returned successfully!')
        else:
            print('This vehicle is already returned. ')

    def calculate_rent(self,days):
        return self.rent_per_day * days

# Child class

class Car(Vehicle):
    def __init__(self,vehicle_id, brand,rent_per_day, seat):
        super().__init__( vehicle_id , brand, rent_per_day)
        self.seat = seat

    def display_info(self):
        super().display_info()
        print(f'Seat : {self.seat}')

# Child class 

class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, rent_per_day, engine_cc):
        super().__init__(vehicle_id, brand, rent_per_day)
        self.engine_cc = engine_cc

    def display_info(self):
        super().display_info()
        print(f'Engine : {self.engine_cc}')

# object for parent class  
c1 = Vehicle('109', 'toyota', 2000)
b1 = Vehicle('16', 'Honda', 1000)

# object for child classes
ca1 = Car('12', 'civic', 3000, 5)
bi1 = Bike('15', 'yamaha', 1500, '1300CC')

vehicles = [c1, b1, ca1, bi1]

# Main menu

def main_menu():
    while True:
        print('==== Vehicle Rental System ====')
        print('1. View Vehicle')
        print("2. Rent Vehicle")
        print('3. Calculate Rent')
        print("4. Return Vehicle")
        print('5. save and exit')

        choice = int(input('Enter your choice : '))
        print(choice)

        if choice == 1:
            for vehicle in vehicles:
                vehicle.display_info()
                print()
                
        elif choice == 2:
            vehicle_id = input('Enter vehicle id : ')

            for vehicle in vehicles:
                if vehicle.vehicle_id == vehicle_id:
                    vehicle.rent_vehicle()
        
        elif choice == 3:
            vehicle_id = input('Enter vehicle id : ')
            days = int(input('Enter number of days : '))

            for vehicle in vehicles:
                if vehicle.vehicle_id == vehicle_id:
                    total = vehicle.calculate_rent(days)
                    print(f'Total rent : {total}')
                
        elif choice == 4:
            vehicle_id =input('Enter vehicle id : ')

            for vehicle in vehicles:
                if vehicle.vehicle_id == vehicle_id:
                    vehicle.return_vehicle()

        elif choice == 5:
            print('Thank youfor using the vehicle system.')
            break
        else:
            print('Please enter a valid choice!')

main_menu()
