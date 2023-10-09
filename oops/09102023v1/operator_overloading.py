'''
+ => __add__
- => __sub__
* => __mul__
> => __gt__
< => __lt __
'''
class A:
    def __init__(self,a):
        self.a = a
    def __add__(self,other):
        return A(self.a + other.a)

    def __lt__(self,other):
        if self.a < other.a:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.a > other.a:
            return True
        else:
            return False


obj1 = A(10)
obj2 = A(20)

obj3 = obj1+obj2
print(obj1.a)
print(obj2.a)
print(obj3)
print(obj3.a)
print("-----------------")
#less than 
print(obj1 < obj2)
print("-----------------")
#greater than 
print(obj1 > obj2)
