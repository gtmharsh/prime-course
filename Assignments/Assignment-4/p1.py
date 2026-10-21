'''
Create a BankAccount class with attributes acc_no, owner_name, and balance
Add methods to deposit, withdraw, and check_balance
'''

class BankAccount:
    def __init__(self, acc_no, owner_name, balance):
        self.acc_no = acc_no
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount should be positive")
            return
        
        self.balance = self.balance + amount
        print(f"Successfully deposited {amount}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawl amount should be positive.")
            return

        if amount > self.balance:
            print("Insufficient Balance")
            return
        
        self.balance -= amount
        print(f"Successfully withdrawn {amount}")

    def check_balance(self):
        print(f"Account Holder: {self.owner_name}\n"
              f"Account Number: {self.acc_no}\n"
              f"Account Balance: {self.balance:.2f}\n")


if __name__ == "__main__":
    acc = BankAccount(1001, "NoOne", 10000)

    acc.check_balance()

    print("\n--- Depositing ---")
    acc.deposit(500)
    acc.check_balance()

    print("\n--- Withdrawl ---")
    acc.withdraw(200)
    acc.check_balance()


    print("\n--- Testing invalid withdrawal ---")
    acc.withdraw(20000)
    acc.withdraw(-100)

    print("\n--- Testing invalid deposit ---")
    acc.deposit(-100)