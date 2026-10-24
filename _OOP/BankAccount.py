class BankAcount:
    
    def __init__(self,init_rate,balance=0):
        self.init_rate=init_rate/100
        self.balance=balance
        
    def deposite(self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amout):
        if self.balance>amout:
            self.balance-=amout
        else:
            print("insufficient funds:Charging a $5 fee")
            self.balance-=5            
        return self
    def display_account_info(self):
        print(f"Balance : $ {self.balance}")
        return self
    def yield_intrest(self):
        self.balance+=(self.init_rate*self.balance)       
        return self
        
accounr1=BankAcount(init_rate=1,balance=100000)        
accounr2=BankAcount(init_rate=1,balance=20000)
accounr1.deposite(5000).deposite(2000).deposite(1000).withdraw(20000).yield_intrest().display_account_info()
accounr2.deposite(5000).deposite(1000).withdraw(2000).withdraw(10000).withdraw(1000).withdraw(500).yield_intrest().display_account_info()
 