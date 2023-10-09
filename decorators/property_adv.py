# senario: i want to change method at object level 

class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    @property
    def msg(self):
        return self.name + "Got Grade" + self.Grade
    def msg(self,msg):
        """
        Want to overwrite self.name and self.grade from msg at runtime
        `msg=Murali Got Grade A`
        """
        updated = msg.split(" ")
        self.name = updated[0]
        print(updated)
        #find above doc msg
        self.grade = updated[-1]

print("Before Overwrite msg:")
print('-'*20)
std1 = Student("Satya","B")
print("Student Name: ",std1.name)
print("Student Grade: ",std1.grade)
print()
#self.name + "Got Grade" + self.Grade follow structure
print('*'*30)
print()
print("After Overwriting msg:")
print('-'*20)
std1.msg("Murali Got Grade A")
print("Student Name: ",std1.name)
print("Student Grade: ",std1.grade)
print(Student.msg.__doc__)