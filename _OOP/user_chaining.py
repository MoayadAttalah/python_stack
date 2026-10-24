class User:
    def __init__(self,user_balance):
        self.user_balance=user_balance
        
    def make_adeposit(self,amount):
        self.user_balance+=amount
        return self                      ##########################i should return self to be able to use chaining method  
        
    def make_withdrawal(self,amount):
        self.user_balance-=amount
        return self    
        
    def display_user_balance(self):
        print(self.user_balance)  
        return self    

    def transfer_money(self,other_user,amount):
        self.user_balance-=amount
        other_user.user_balance+=amount          
        return self    
        

moayad=User(20000)
ahmad=User(10000)
sara=User(50000)
moayad.make_adeposit(1000).make_adeposit(1500).make_adeposit(2000).make_withdrawal(5000).display_user_balance()
ahmad.make_adeposit(500).make_adeposit(500).make_withdrawal(1000).make_withdrawal(1200).display_user_balance()
sara.make_adeposit(500).make_withdrawal(2500).make_withdrawal(1200).display_user_balance()
sara.transfer_money(moayad,10000)
moayad.display_user_balance()
sara.display_user_balance()          