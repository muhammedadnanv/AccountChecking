class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. Your new balance is ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. Your new balance is ${self.balance}")
        else:
            print("Insufficient funds")

def login():
    # Hardcoded login credentials for demonstration purposes
    email = " adnanmuhammad4393@gmail.com"
    password = " adnanmuhammad4393@gmail.compassword"

    while True:
        input_email = input("Enter email: ")
        input_password = input("Enter password: ")

        if input_email == email and input_password == password:
            print("Login successful!")
            return True
        else:
            print("Invalid email or password. Please try again.")

def main():
    if not login():
        print("Login failed. Exiting...")
        return

    atm = ATM()
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
