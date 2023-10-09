'''static method we can decalre in the class
there self is not needed.
but we can call it via Class or object.using decorator'''

class Dev:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    @staticmethod
    def instituteName():
        print("Ineuron.ai")
v=Dev("satya","DevOps")
print(v.name,v.course)
# #static methods
Dev.instituteName()
v.instituteName()
