class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
obj = A(10,20)
print(obj)

'''<__main__.A object at 0x00000211BCCFF810>
it will printing memory like above to avoid this use __str__ we are overding useing this str construct'''

#task1: 
class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f'{self.a}--->{self.b}'
obj = A(10,20)
print(obj)

#task 2:

class Info:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name}.{self.last_name}'

name = Info("Satya","Peddireddi")
print(name)
