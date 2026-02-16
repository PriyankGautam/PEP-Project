class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount} successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount} successfully.")
        else:
            print("Insufficient balance or invalid amount!")

    def display(self):
        print("------ Account Details ------")
        print("Name:", self.name)
        print("Balance: ₹", self.__balance)
        print("-----------------------------")



acc1 = BankAccount("Priyank", 5000)

acc1.display()
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.display()
