'''5 types 
1) single level inheritance
2) multi level inheritance
3) multiple inheritance
4) heirarchical inheritance
5) hybrid inheritance
we can avoid code duplicate parent and child classes
'''
class A:
    def __init__(self,a_class):
        self.a = a_class
    def print_a(self):
        print("A Value: ", self.a)
class B(A): # single level inheritance
    def __init__(self,a_class,b_class):
        A.__init__(self,a_class) # need to call calss A values
        self.b = b_class
    def print_b(self):
        print("B Value: ", self.b)

obj1 = B(20,30)
obj1.print_a()
obj1.print_b()