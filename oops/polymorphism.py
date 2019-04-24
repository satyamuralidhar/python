class Shape:
    width = 0
    height = 0

    def area(self):
        print("This is about polymorphisam")
class Rectangle:
    def __init__(self ,w, h):
        self.width = w
        self.height = h
    def area(self):
         print("Area of Rectangle is:", self.width * self.height)
class Triangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
    def area(self):
        print("Area of triangle is:", (self.width * self.height)/2)
rect = Rectangle(20,30)
rect.area()
tri = Triangle(30,40)
tri.area()

