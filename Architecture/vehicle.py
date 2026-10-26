
class Vehicle:

    def __init__(self):
        print("\n-- Register Vehicle --")

        self.vehicle_id = input("Enter Vehicle ID: ").strip()
        self.vehicle_number = input("Enter Vehicle Number: ").strip().upper()

        while True:
            self.vehicle_type = input(
                "Enter Vehicle Type (Bike/Auto/Car): "
            ).strip().capitalize()#removing spaces and making the first letter Capital

            if self.vehicle_type in ["Bike", "Auto", "Car"]:
                break # if the vehicle type is correct the loop gets breaked and the value is Stored

            print("Invalid vehicle type! Choose Bike, Auto, or Car.")

        self.vehicle_model = input("Enter Vehicle Model: ").strip()
        self.vehicle_color = input("Enter Vehicle Color: ").strip()

        self.available = True

    def vehicle_details(self):
        print("\n-- Vehicle Details --")
        print(f"Vehicle ID     : {self.vehicle_id}")
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Vehicle Type   : {self.vehicle_type}")
        print(f"Vehicle Model  : {self.vehicle_model}")
        print(f"Vehicle Color  : {self.vehicle_color}")
        print(f"Availability   : {'Available' if self.available else 'In Use'}")

    def update_vehicle(self):

        while True:
            choice = input("""
        -- Update Vehicle Details --

        Enter 1 to Vehicle Number
        Enter 2 to Vehicle Type
        Enter 3 to Vehicle Model
        Enter 4 to Vehicle Color
        5. Back
        """)


            if choice == "1":
                new_number = input("Enter New Vehicle Number: ").strip()

                if new_number:
                    self.vehicle_number = new_number.upper()
                    print("Vehicle number updated successfully!")
                else:
                    print("Vehicle number cannot be empty.")

            elif choice == "2":
                new_type = input(
                    "Enter New Type (Bike/Auto/Car): "
                ).strip().capitalize()

                if new_type in ["Bike", "Auto", "Car"]:
                    self.vehicle_type = new_type
                    print("Vehicle type updated successfully!")
                else:
                    print("Invalid vehicle type!")

            elif choice == "3":
                new_model = input("Enter New Vehicle Model: ").strip()

                if new_model:
                    self.vehicle_model = new_model
                    print("Vehicle model updated successfully!")
                else:
                    print("Model cannot be empty.")

            elif choice == "4":
                new_color = input("Enter New Vehicle Color: ").strip()

                if new_color:
                    self.vehicle_color = new_color
                    print("Vehicle color updated successfully!")
                else:
                    print("Color cannot be empty.")

            elif choice == "5":
                return

            else:
                print("Invalid choice! Please try again.")

vehicle1 = Vehicle()
vehicle1.vehicle_details()