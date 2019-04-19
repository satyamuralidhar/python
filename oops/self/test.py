from _ctypes_test import func


class Satya:
    ''' this is all about satya's information'''

    def __init__(self ,name,surname):
        self.name = name
        self.surname = surname
    def info(self):
         print('naam:', self.name)
         print('pura naam:', self.surname)

class Ram():    
    def func(self):
         print("hi murali how r u")
         print(Satya.__doc__)
         help(Satya)

s1 = Satya("muralidhar " , "peddireddi")
s2 = Satya("mohan" , "peddireddi")
s1.info()
s2.info()
sam = Ram()
sam.func()

