
from vehicle import Vehicle
from driver import Driver

print("STEP 1: Creating vehicle")
vehicle1 = Vehicle()

print("STEP 2: Creating driver")
driver1 = Driver()

print("STEP 3: Assigning vehicle")
driver1.assign_vehicle(vehicle1)

print("STEP 4: Opening driver menu")
driver1.driver_menu()

print("STEP 5: Program finished")
