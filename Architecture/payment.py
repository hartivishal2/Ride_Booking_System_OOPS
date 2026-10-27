class Payment:

    def __init__(self , payment_id ,ride):
        self.payment_id = payment_id
        self.ride = ride
        self.amount = ride.fare 
        self.payment_method = None
        self.status = "Pending"

    def select_payment_method(self):

        while True :
            choice = input("""
                    -- Payment Method --

                    1. Cash
                    2. Upi(PhonePe , GooglePay)
                    3. Card


                    """
            )
            if choice == "1" :
                self.payment_method = "Cash"
                break
            elif choice == "2" :
                self.payment_method = "UPI"
                break
            elif choice == "3" :
                self.payment_method = "Card"
                break
            else :
                print("Invalid Payment Method Choosen ! Try Again .")
                

            print(f"The payment Method is Selected as {self.payment_method}")

    def make_payment(self):

        if self.ride.status != "Completed" :
            print("\nLet the ride be completed ! You can pay After you Reach")
            return 
        
        if self.payment_method is None :
            print("\nPlease Select the Payment Method to Continue...!")
            return 
        
        if self.status == "Paid" :
            print("\n The payment Has been done . Thank Youii..")

        self.status = "Paid"

        print("\nPayment successful!")

    def payment_details(self):

        print("\n-- Payment Details --")
        print(f"Payment ID : {self.payment_id}")
        print(f"Ride ID : {self.ride.ride_id}")
        print(f"Passenger : {self.ride.user.username}")
        print(f"Amount : ${self.amount:.2f}")
        print(f"Payment Method : {self.payment_method}")
        print(f"Payment Status : {self.status}")

        