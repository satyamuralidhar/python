class Ranjith:
    '''this is sample information'''
    def __init__(self , first , last):
        self.first = first
        self.last = last
        self.email = first +'.'+ last +'@gmail.com'    
    def fullname(self):
        return '{} {}'.format(self.first , self.last)
class Satya:
    def __init__(self , age):
        self.age = age    
    @property    
    def years(self):
        return '{}'.format(self.age)    
ram = Ranjith('muralidhar' , 'peddireddi')
sam = Satya(10)
print(Ranjith.__doc__)
print(ram.email)
print(ram.fullname)
print(sam.years)
class Ramana:
    ''' This is All about Ramana's information '''
    def __init__(self, name , surname):
        self.name = name
        self.surname = surname
    @property
    def fullname2(self):
        return '{} {}'.format(self.name , self.surname) 
x = Ramana('ramana' ,'grandhi')
print(Ramana.__doc__)
print(x.name)
print(x.fullname2)
class Vijay:
    print('Hi this is vijay')
    @property
    def __init__(self , study , job):
        self.study = study
        self.job = job
    def v1(self):
        return '{} {}'.format(self.study , self.job)    
    def __init__(self , monthlysalary , anualsalary):
        self.monthlysalary = monthlysalary
        self.anualsalary = anualsalary
    def v2(self):
        return '{} {}'.format(self.monthlysalary , self.anualsalary)    
class lakshman(Vijay):
    '''::: Hi this is lakshman child of Vijay :::'''
    print("hi this is lakshman") 
y = Vijay(40000 , 500000)
y.v1
z = lakshman
z.v2
A = Vijay("B-tech" , "Engineer")   
A.v1    
print(lakshman.__doc__)  
