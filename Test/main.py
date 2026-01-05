class BankAccount:

    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
   

    def deposit(self, amount):
        if amount < 0:
            return "Invalid Amount Entered"
        else:
            self.balance += amount
        return {"Total Available Balance": self.balance}
    
    def withdraw(self, amount):
        if self.balance < amount:
            return "The amount you entered is less than your balance"
        else:
            self.balance -= amount
        return {"Total Available Balance" : self.balance}
    
    def display(self):
        print("Account Holder :", self.account_holder)
        print("Account Number:", self.account_number)
        print("Available Balance: ", self.balance)
    

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, minimum_balance):
        super().__init__(account_number, account_holder, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if amount<= 0:
            raise ValueError("Amount is less than zero")
        
        if amount> self.balance:
            raise ValueError("You don't have enough balnce to withdraw")
        
        if self.balance-amount<self.minimum_balance:
            raise ValueError("You must maintain your minimum balance")
        self.balance -= amount

bank = []

bank.append(BankAccount(123, 'Sindhu', 5000))
bank.append(SavingsAccount(124, 'Sameera', 8000, 3000))
try:
    bank[0].deposit(2000)
    bank[1].withdraw(4000)
except ValueError as e:
    print(e)

for x in bank:
    x.display()
