class BankAccount:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Balance for account {self.acc_number}: {self.balance}")



account_number = int(input("Enter the account number: "))
balance = int(input("Enter the initial balance: "))

acc = BankAccount(account_number, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        acc.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        acc.withdraw(amount)

    elif choice == 3:
        acc.display_balance()

    elif choice == 4:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice")
