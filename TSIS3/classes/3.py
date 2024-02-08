class Shape:
    def __init__(self) -> None:
        self.areadef = 0
    def area(self):
        print(self.areadef)

class Rectangle(Shape):
    def __init__(self,length,width) -> None:
        self.length = length
        self.width = width
        self.areadef = length * width

ob2 = Rectangle(4,5)
ob2.area()