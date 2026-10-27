from user import User
from vehicle import Vehicle
from driver import Driver
from ride import Ride
from payment import Payment


# STEP 1: Create a passenger
print("\n-.-.-.-.-.- STEP 1: REGISTER PASSENGER -.-.-.-.-.-")
user1 = User(
    "U101",
    "Rahul",
    "9876543210",
    "rahul@gmail.com"
)
print("Passenger registered successfully!")


# STEP 2: Register a vehicle
print("\n-.-.-.-.-.- STEP 2: REGISTER VEHICLE -.-.-.-.-.-")
vehicle1 = Vehicle()
print("Vehicle registered successfully!")


# STEP 3: Register a driver
print("\n-.-.-.-.-.- STEP 3: REGISTER DRIVER -.-.-.-.-.-")
driver1 = Driver()
print("Driver registered successfully!")


# STEP 4: Assign vehicle to driver
print("\n-.-.-.-.-.- STEP 4: ASSIGN VEHICLE -.-.-.-.-.-")
driver1.assign_vehicle(vehicle1)


# STEP 5: Create a ride request
print("\n-.-.-.-.-.- STEP 5: BOOK A RIDE -.-.-.-.-.-")
ride1 = Ride(
    "R101",
    user1,
    "Pune Station",
    "Hinjawadi",
    10
)
print("Ride requested successfully!")


# STEP 6: Assign driver to ride
print("\n-.-.-.-.-.- STEP 6: ASSIGN DRIVER TO RIDE -.-.-.-.-.-")
ride1.assign_driver(driver1)


# STEP 7: Display ride details and fare
print("\n-.-.-.-.-.- STEP 7: RIDE DETAILS -.-.-.-.-.-")
ride1.ride_details()

print("\n-.-.-.-.-.- RIDE BOOKING PROCESS FINISHED -.-.-.-.-.-")


# STEP 8: Complete the ride
print("\n-.-.-.-.-.- STEP 8: COMPLETE RIDE -.-.-.-.-.-")
ride1.complete_ride()

# STEP 9: Display final ride status
print("\n-.-.-.-.-.- STEP 9: FINAL RIDE STATUS -.-.-.-.-.-")
ride1.ride_details()

# STEP 10: Create payment
print("\n-.-.-.-.-.- STEP 10: CREATE PAYMENT -.-.-.-.-.-")

payment1 = Payment(
    "P101",
    ride1
)

print("Payment created successfully!")


# STEP 11: Select payment method
print("\n-.-.-.-.-.- STEP 11: SELECT PAYMENT METHOD -.-.-.-.-.-")

payment1.select_payment_method()


# STEP 12: Make payment
print("\n-.-.-.-.-.- STEP 12: MAKE PAYMENT -.-.-.-.-.-")

payment1.make_payment()


# STEP 13: Display payment details
print("\n-.-.-.-.-.- STEP 13: PAYMENT DETAILS -.-.-.-.-.-")

payment1.payment_details()


# Final message
print("\n-.-.-.-.-.- RIDE BOOKING PROCESS FINISHED -.-.-.-.-.-")
