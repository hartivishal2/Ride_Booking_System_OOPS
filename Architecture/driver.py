from user import User 
#using the user part of the code to inherit the input part that we need
#to assign to the driver as driver is also a type of user and same details 
#will be required 

class Driver(User):

    def __init__(self):
        print("\n-- Register Driver --")

        # Common details inherited from User
        user_id = input("Enter User ID: ").strip()
        username = input("Enter Driver Name: ").strip()
        phone = input("Enter Phone Number: ").strip()
        email = input("Enter Email ID: ").strip()

        # Initialize User attributes
        super().__init__(user_id, username, phone, email)

        # Driver-specific details
        self.driver_id = input("Enter Driver ID: ").strip()

        # No vehicle assigned initially
        self.vehicle = None

        # Driver availability
        self.available = True

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        print("\nVehicle assigned to driver successfully!")

    def driver_details(self):
        print("\n-- Driver Details --")
        print(f"Driver ID    : {self.driver_id}")
        print(f"User ID      : {self.user_id}")
        print(f"Driver Name  : {self.username}")
        print(f"Phone Number : {self.phone}")
        print(f"Email        : {self.email}")
        print(f"Availability : {'Available' if self.available else 'Busy'}")

        if self.vehicle is not None:
            print("\n-- Assigned Vehicle --")
            self.vehicle.vehicle_details()
        else:
            print("Vehicle      : Not Assigned")

    def update_driver(self):
        while True:
            choice = input("""
        -- Update Driver Details --

        1. Update Driver Name
        2. Update Phone Number
        3. Update Email
        4. Update Driver ID
        5. Back

        Enter your choice: """)

            if choice == "1":
                new_name = input("Enter New Driver Name: ").strip()
                if new_name:
                    self.username = new_name
                    print("Driver name updated successfully!")
                else:
                    print("Name cannot be empty.")

            elif choice == "2":
                new_phone = input("Enter New Phone Number: ").strip()
                if new_phone:
                    self.phone = new_phone
                    print("Phone number updated successfully!")
                else:
                    print("Phone number cannot be empty.")

            elif choice == "3":
                new_email = input("Enter New Email ID: ").strip()
                if new_email:
                    self.email = new_email
                    print("Email updated successfully!")
                else:
                    print("Email cannot be empty.")

            elif choice == "4":
                new_id = input("Enter New Driver ID: ").strip()
                if new_id:
                    self.driver_id = new_id
                    print("Driver ID updated successfully!")
                else:
                    print("Driver ID cannot be empty.")

            elif choice == "5":
                return

            else:
                print("Invalid choice! Please try again.")

    def driver_menu(self):
        while True:
            choice = input("""
        -- Driver Menu --

        1. View Driver Details
        2. Update Driver Details
        3. View Assigned Vehicle
        4. Change Availability
        5. Exit

        Enter your choice: """)

            if choice == "1":
                self.driver_details()

            elif choice == "2":
                self.update_driver()

            elif choice == "3":
                if self.vehicle is not None:
                    self.vehicle.vehicle_details()
                else:
                    print("\nNo vehicle assigned yet.")

            elif choice == "4":
                self.available = not self.available
                status = "Available" if self.available else "Busy"
                print(f"\nDriver status changed to: {status}")

            elif choice == "5":
                print("\nExiting Driver Menu...")
                return

            else:
                print("\nInvalid choice! Please try again.")


