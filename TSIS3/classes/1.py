class Myclass:
    def __init__(self):
        self.name = ""
        self.surname = ""
    def getString (self):
        self.name = input()
        self.surname = input()
    def printString(self):
        print(self.name.upper(),self.surname.upper())
p1 = Myclass()
p1.getString()
p1.printString()
