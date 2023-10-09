#senario : check a driving licence is valid or not.

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
            
user1 = Vehical("Satya","Peddireddi",28,1234,499,2024,"AP5 01 2868","5years")
user2 = Vehical("Ram","reddy",30,1256,501,2023,"TN 8t 6985","2years")
'''checking valid driver or not'''
print ("Driver Vaildation: {} status {}".format(user2.first_name,user2.is_vaild_driver()))
print ("Driver Vaildation: {} status {}".format(user1.first_name,user1.is_vaild_driver()))