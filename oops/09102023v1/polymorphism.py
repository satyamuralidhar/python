'''
polymorphism has two types:
    method overloading
    method overriding
'''
#method overloading: if one can execute multilpe valoues if values not avaible it it taken default values.
#if x value is not entered it will takes default value which are entered in function.abs

def add(a,b,c,d,x=0,y=1,z=2):
    addition = a+b+c+d+x+y+z
    print("value: ",addition)
add(1,2,3,4)
add(1,2,3,4,5)
add(1,2,3,4,5,6)

'''method over riding
we can override a method if method values not exist in child it will takes values form parent'''


class Father:
    def __init__(self):
        pass

    def Height(self):
        print("Height: ", 5.7)

    def Age(self):
        print("Age: ", 58)

    def Education(self):
        print("Education: ", "B tech")

    def Stream(self):
        print("Stream: ", "Electronics")

class Son(Father):
    def __init__(self):
        Father.__init__(self)

    def Height(self):
        print("Height: ", 5.5)

    def Age(self):
        print("Age: ", 29)

    def Education(self):
        print("Education: ", "Degree")

    def City(self):
        print("City: ","Hyd")

father = Father()
son = Son()
print("---------------------")
father.Height()
father.Age()
father.Education()
print("---------------------")
son.Height()
son.Age()
son.Education()
son.Stream() # Stream method not in Son class it will take it form father Class .
son.City()


