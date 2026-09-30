#       BANKING MANAGEMENT SYSTEM
class Account:
    def __init__(self, account_no, name, pin, balance):
        self.account_no = account_no
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = []
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append("Deposited:  Rs.{amount}")
            print("Money deposited successfully!")
        else:
            print("Invalid amount.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ₹{amount}")
            print("Money withdrawn successfully!")
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
    def show_details(self):
        print("              ACCOUNT DETAILS                   ")
        print("Account Number:", self.account_no)
        print("Name:", self.name)
        print("Balance: Rs. ", self.balance)
    def show_transactions(self):
        print("               TRANSACTIONS                ")
        if len(self.transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)
# Store all accounts
accounts = {}
# Starting account number
next_account_number = 1001
# CREATE ACCOUNT
def create_account():
    global next_account_number
    print("               CREATE ACCOUNT            ")

    name = input("Enter your name: ")
    pin = input("Create a 6-digit PIN: ")
    if len(pin) != 6 or not pin.isdigit():
        print("PIN must contain exactly 6 digits.")
        return
    try:
        balance = float(input("Enter initial deposit: ₹"))
    except ValueError:
        print("Please enter a valid amount.")
        return
    if balance < 0:
        print("Balance cannot be negative.")
        return
    account = Account(next_account_number,name,pin,balance )
    accounts[next_account_number] = account
    print("Account created successfully!")
    print("Your Account Number is:", next_account_number)
    next_account_number += 1
# LOGIN
def login():
    print("LOGIN")
    try:
        account_no = int(input("Enter Account Number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if account_no not in accounts:
        print("Account not found.")
        return

    account = accounts[account_no]

    pin = input("Enter the  PIN: ")
    if pin != account.pin:
        print("Invalid Pin")
        return

    print("Welcome, {account.name}!")
    account_menu(account)
# ACCOUNT MENU
def account_menu(account):

    while True:
        print("               ACCOUNT MENU            ")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Account Details")
        print("5. Transaction History")
        print("6. Logout")

        choice = input(" Enter your choice: ")

        if choice == "1":

            try:
                amount = float(
                    input("Enter amount to deposit: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            account.show_details()
        elif choice == "5":
            account.show_transactions()
        elif choice == "6":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice.")
# MAIN PROGRAM
def main():
    while True:
        print(" BANKING MANAGEMENT SYSTEM")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your option: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            print(" Thank you for using our Banking System!")
            break
        else:
            print("Invalid choice. Please try again.")
# Start the program
main()