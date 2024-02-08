from math import sqrt
class Point :
    def __init__(self,x , y) -> None:
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def move(self,x,y):
        self.x+=x
        self.y+=y
    def dist(self , x2 , y2):
        print(sqrt((y2-self.y)**2+(x2-self.x)**2))
    
ob = Point(1,0)
ob.dist(2,0)
