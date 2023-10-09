'''combination of atleast two
hierarchical:
=============
parent: vehicle
sub: bus,Auto
A Parent --> B(A) --> C(A) or --> D(A)
class Bus(vehicle)
class Auto(Vehicle)

multiple:
=======
parent:  vehicle,Diesel
sub : bus

Hybrid: 
At least two inheritance type
class Bus(Vehical,Diesel):
class Auto(Vehical,Diesel):
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

'''creating mutliple inheritance from above classes
 '''

class Diesel:
    def __init__(self,price):
        self.price = price

class Bus(Vehical,Diesel):
    def __init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age,price,wheels):
        Vehical.__init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age)
        Diesel.__init__(self,price)
        self.wheels = wheels  

    def Diesel_Price_vehicle(self):
        if self.price >= 90:
            return f'{self.price}-INR'
        else:
            return "Price is Below 90rs"

class Auto(Vehical,Diesel):
    def __init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age,price,wheels):
        Vehical.__init__(self,first_name,last_name,age,contact,id,validity,vehical_number,vehical_age)
        Diesel.__init__(self,price)
        self.wheels = wheels  

    def Wheels(self):
        if self.wheels == 4:
            return "Four Wheeler"
        else:
            return "Auto"


user1 = Bus("Satya","Peddireddi",28,1234,499,2024,"AP5 01 2868","5years",110,4)
user2 = Auto("Ram","reddy",30,1256,501,2023,"TN 8T 9785","2years",95,3)
'''checking valid driver or not'''
print ("Driver Vaildation: {} status {}".format(user2.first_name,user2.is_vaild_driver()))
print ("Driver Vaildation: {} status {}".format(user1.first_name,user1.is_vaild_driver()))
#diesel price
print("Diesel Rate: BusNumber: '{}' Rate: '{}'".format(user1.vehical_number,user1.Diesel_Price_vehicle()))
#print("Diesel Rate: AutoNumber: '{}' Rate: '{}'".format(user2.vehical_number,user2.Diesel_Price_vehicle()))
#vehicle type
print("AutoNumber: '{}' Vehicle Type: '{}'".format(user2.vehical_number,user2.Wheels()))
#print("BusNumber: '{}' Vehicle Type: '{}'".format(user1.vehical_number,user1.wheels()))