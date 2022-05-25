class make_withdraw:
    def __init__(self, balance):
        self.balance = balance
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return 'Insufficient funds'
