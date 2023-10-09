'''hierarchical:
=============
parent: vehicle
sub: bus,Auto
A Parent --> B(A) --> C(A) or --> D(A)
class Bus(vehicle)
class Auto(Vehicle)
'''
class Driver:
    def __init__(self,first_name,last_name,age,contact):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.contact = contact

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

class Licence(Driver):
    def __init__(self,first_name,last_name,age,contact,id,validity):
        Driver.__init__(self,first_name,last_name,age,contact)
        self.id = id
        self.validity = validity

    def is_valid_licence(self):
        if self.validity >= 2024:
            return True
        else:
            return False

class Vehical(Licence):
    def __init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age):
        Licence.__init__(self,first_name,last_name,age,contact,id,validity)
        self.vehical_age = vehical_age
        self.vehical_number = vehical_number

    def is_vaild_driver(self):
        if self.age >= 20:
            return "Valid"
        else:
            return "Not Valid"


class Bus(Vehical):
    def __init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age,Buswheels):
        Vehical.__init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age)
        self.Buswheels = Buswheels  



class Auto(Vehical):
    def __init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age,Autowheels):
        Vehical.__init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age)
        self.Autowheels = Autowheels  

transport1 = Bus("Satya","Peddireddi",28,1234,499,2024,"AP05 01 2868","5years",4)
transport2 = Auto("Mohan","Peddireddi",30,1247,182,2023,"TN04 06 8629 ","2years",3)

print("Vehicle Type: {} wheeler".format(transport2.Autowheels))

print("Vehicle Type: {} wheeler".format(transport1.Buswheels))
