class User:

    def __init__(self):
        print("\nPlease Enter the Following Details to Proceed!")

        self.user_id = input("Enter User ID: ")
        self.username = input("Enter Username: ")
        self.phone = input("Enter Phone Number: ")
        self.email = input("Enter Email ID: ")

        self.menu()

    def menu(self):

        while True:

            num_input = input("""
        ** -- Welcome to our Booking System -- **

        Press 1 to See Your Profile
        Press 2 to Update Your Profile
        Press 3 to Exit

        Enter your choice: 
        """)

            if num_input == "1":
                self.profile()

            elif num_input == "2":
                self.update_profile()

            elif num_input == "3":
                print("\nThank you for using our Booking System!")
                return

            else:
                print("\nInvalid choice! Please try again.")

    def profile(self):
        print("\n-- Profile --")
        print(f"USER ID   :- {self.user_id}")
        print(f"USERNAME  :- {self.username}")
        print(f"PHONE NO  :- {self.phone}")
        print(f"EMAIL ID  :- {self.email}")

    def update_profile(self):
        print("\n-- Updating the Profile --")

        self.user_id = input("Enter New User ID: ")
        self.username = input("Enter New Username: ")
        self.phone = input("Enter New Phone Number: ")
        self.email = input("Enter New Email ID: ")

        print("\nProfile updated successfully!")

