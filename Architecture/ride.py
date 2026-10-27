class Ride:
    def __init__(self, ride_id, user, pickup, destination, distance):
        self.ride_id = ride_id
        self.user = user
        self.pickup = pickup
        self.destination = destination
        self.distance = distance

        self.driver = None
        self.fare = 0
        self.status = "Requested"
        
    def assign_driver(self, driver):
        if not driver.available:
            print("This driver is currently unavailable.")
            return

        self.driver = driver
        driver.available = False
        self.status = "Accepted"

        print("Driver assigned successfully!")

    def calculate_fare(self):
        base_fare = 50
        rate_per_km = 15

        self.fare = base_fare + (self.distance * rate_per_km)

        return self.fare

    def ride_details(self):
        print("\n-- Ride Details --")
        print(f"Ride ID : {self.ride_id}")
        print(f"Passenger : {self.user.username}")
        print(f"Pickup  : {self.pickup}")
        print(f"Destination : {self.destination}")
        print(f"Distance : {self.distance} km")
        print(f"Fare : ₹{self.calculate_fare():.2f}")
        print(f"Ride Status : {self.status}")

        if self.driver is not None:
            print(f"Driver : {self.driver.username}")
            print(f"Driver ID : {self.driver.driver_id}")
        else:
            print("Driver : Not Assigned")


    def complete_ride(self):
        if self.driver is None:
            print("Cannot complete ride: No driver assigned.")
            return

        if self.status == "Completed":
            print("This ride is already completed.")
            return

        self.status = "Completed"
        self.driver.available = True

        if self.driver.vehicle is not None:
            self.driver.vehicle.available = True

        print("\nRide completed successfully!")
        print("Driver is now available for another ride.")

