class User:
    def __init__(self,user_balance):
        self.user_balance=user_balance
        
    def make_adeposit(self,amount):
        self.user_balance+=amount
            
        
    def make_withdrawal(self,amount):
        self.user_balance-=amount
        
    def display_user_balance(self):
        print(self.user_balance)  
    
    def transfer_money(self,other_user,amount):
        self.user_balance-=amount
        other_user.user_balance+=amount          
        

moayad=User(20000)
ahmad=User(10000)
sara=User(50000)
moayad.make_adeposit(1000)
moayad.make_adeposit(1500) 
moayad.make_adeposit(2000)
moayad.make_withdrawal(5000)
moayad.display_user_balance()
ahmad.make_adeposit(500)
ahmad.make_adeposit(500) 
ahmad.make_withdrawal(1000)
ahmad.make_withdrawal(1200)
ahmad.display_user_balance()
sara.make_adeposit(500)
sara.make_withdrawal(2500)
sara.make_withdrawal(1200)
sara.display_user_balance()
sara.transfer_money(moayad,10000)
moayad.display_user_balance()
sara.display_user_balance()          