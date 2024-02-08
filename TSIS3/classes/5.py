class Account :
    def __init__(self, owner , balance ) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self) :
        self.balance += int(input("balance:"))

    def withdraw (self):
        withdrawal=int(input("withdrawal:"))
        if (self.balance < withdrawal ):
            print("Cant take it!")
        else :
            self.balance-=withdrawal


