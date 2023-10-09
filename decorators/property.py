# updating values on attribute level.abs
#note: execute stage by stage comment another stage


'''stage1:'''

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.msg = self.name + " Got Grade " + self.grade

std1 = Student('Satya',"B")
std1.grade = "A" #trying to updating the grade
print("Name:",std1.name)
print("Grade:",std1.grade)
print(std1.msg)
'''
o/p
-------------
Name: Satya
Grade: A
Satya Got Grade B

not updated grade in msg level 
lets try to use to update method level
'''

'''stage2:'''

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    def msg(self):
        return self.name + " Got Grade " + self.grade

std1 = Student("Satya","B")
print("Name:",std1.name)
print("Grade:",std1.grade)
print(std1.msg)
print(std1.msg())
'''
std1.msg is <bound method Student.msg of <__main__.Student object at 0x000001C810930110>>
its printing memory of msg method to use method use std.msg()

propery decorator is change the class with out effecting the client code
'''

'''stage3'''

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    @property
    def msg(self):
        """
        Property Decorator allows us to use method as a atrribute
        """
        return self.name + " Got Grade " + self.grade

print(Student.msg.__doc__)
std1 = Student("Satya","B")
print("Name:",std1.name)
print("Grade:",std1.grade)
print(std1.msg) 
"""
if we use property decorator it will print the value in the pirituclar address.
 dont need to use medthod like std1.msg()
"""
#print(std1.msg())


