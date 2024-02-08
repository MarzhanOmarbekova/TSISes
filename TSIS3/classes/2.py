class Shape:
    def __init__(self) -> None:
        self.areadef = 0
    def area(self):
        print(self.areadef)

class Square(Shape):
    def __init__(self,length):
        self.length = length
        self.areadef = length**2
    
ob = Square(5)
ob.area() 




        
