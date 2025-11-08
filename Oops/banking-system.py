class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debited")
        print("total balance = ", self.balance)
    
    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, "was credited", self.balance)
    
    def get_balance(self):
        return self.balance

acc1 = Account(15000, 12345678)
acc1.debit(500)

acc2 = Account(35000, 7891098)
acc2.debit(2000)