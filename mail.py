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
