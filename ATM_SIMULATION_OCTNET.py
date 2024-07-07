class ATM:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def start(self):
        print("Welcome to ATM Machine")
        pin_entry = input("Enter your PIN: ")
        if pin_entry == str(self.pin):
            print("Login successful!")
            while True:
                print("1. Account Balance Inquiry")
                print("2. Cash Withdrawal")
                print("3. Cash Deposit")
                print("4. PIN Change")
                print("5. Transaction History")
                print("6. Exit")
                option = input("Choose an option: ")
                if option == "1":
                    self.account_balance_inquiry()
                elif option == "2":
                    self.cash_withdrawal()
                elif option == "3":
                    self.cash_deposit()
                elif option == "4":
                    self.pin_change()
                elif option == "5":
                    self.transaction_history()
                elif option == "6":
                    print("Exiting...")
                    break
                else:
                    print("Invalid option. Please try again.")
        else:
            print("Invalid PIN. Please try again.")

    def account_balance_inquiry(self):
        print("Your account balance is: $", self.balance)

    def cash_withdrawal(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if amount > self.balance:
            print("Insufficient balance. Please try again.")
        else:
            self.balance -= amount
            self.transaction_history.append("Withdrawal: -$" + str(amount))
            print("Withdrawal successful. Your new balance is: $", self.balance)

    def cash_deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        self.balance += amount
        self.transaction_history.append("Deposit: +$" + str(amount))
        print("Deposit successful. Your new balance is: $", self.balance)

    def pin_change(self):
        current_pin = input("Enter your current PIN: ")
        if current_pin == str(self.pin):
            new_pin = input("Enter your new PIN: ")
            self.pin = int(new_pin)
            print("PIN changed successfully.")
        else:
            print("Invalid current PIN. Please try again.")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)


atm = ATM("1234567890", 1234, 1000.0)
atm.start()