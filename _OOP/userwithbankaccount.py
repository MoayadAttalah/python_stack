from BankAccount import BankAcount
class User:
    def __init__(self,init_rate,user_balance=0):
        self.user_balance=user_balance
        self.account=BankAcount(init_rate,user_balance)
    def make_adeposit(self,amount):
        self.account.deposite(amount)
        return self 
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self         
    def display_user_balance(self):
        self.account.display_account_info()
        return self 
        
        
moayad=User(init_rate=1,user_balance=20000)        
moayad.make_adeposit(1000).make_adeposit(1500).make_adeposit(2000).make_withdrawal(5000).display_user_balance()



  


