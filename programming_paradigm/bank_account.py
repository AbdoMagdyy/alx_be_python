class BankAccount:
#start by initializing the attributs
    def __init__(self,initial_balance=0):
        self.current_balance = initial_balance
#diposit metod  (it add the money amount to the balance)
    def deposit(self,amount):
        if amount > 0:
            self.current_balance += amount
        else:
            print('Deposit amount be positive')
#withdraw method  (it subtract the amount of the money from the balance)
    def withdraw(self,amount):
        if amount > self.current_balance:
            print('Insufficient funds')
            return True
        elif amount <= self.current_balance:
            self.current_balance -= amount
            return False
        else:
            print('Withdraw amount must be positive')
            return False
#display method  (it display the balance of the account)
    def display(self):
        print(self.current_balance)