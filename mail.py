class Employee:
    def __init__(self , first , last):
        self.first = first
        self.last = last
        self.email = first + '.' + last +'@gmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp = Employee("muralidhar" , "peddireddi")
emp2 = Employee('ramareddy' , "gudla")
print(emp.email)
print(emp.fullname())
print(emp2.first)
print(emp2.last)
print(emp2.fullname())
print(emp2.email)

# property decorator
class Employee:
    def __init__(self , first , last):
        self.first = first
        self.last = last
        self.email = first + '.' + last +'@gmail.com'
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
emp = Employee("muralidhar" , "peddireddi")
emp2 = Employee('ramareddy' , "gudla")
print(emp.email)
print(emp.fullname)
print(emp2.first)
print(emp2.last)
print(emp2.fullname)
print(emp2.email)

#@setter Decorator
class Employee:
    def __init__(self , first , last):
        self.first = first
        self.last = last
        self.email = first + '.' + last +'@gmail.com'
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self , name):
        first , last = name.split(' ')
        self.first = first
        self.last = last

emp = Employee("muralidhar" , "peddireddi")
emp2 = Employee('ramareddy' , "gudla")
emp.fullname = 'mohan peddireddi'
print(emp.email)
print(emp.fullname)
print(emp2.first)
print(emp2.last)
print(emp2.fullname)
print(emp2.email)
