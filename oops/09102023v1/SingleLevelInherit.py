#senario : check a driving License is valid or not.

class Driver:
    def __init__(self,first_name,last_name,age,contact):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.contact = contact
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
class License(Driver):
    def __init__(self,first_name,last_name,age,contact,id,validity):
        Driver.__init__(self,first_name,last_name,age,contact)
        self.id = id
        self.validity = validity

    def is_valid_License(self):
        if self.validity >= 2024:
            return True
        else:
            return False

user1 = License("Satya","Peddireddi",28,1234,499,2024)
user2 = License("Ram","reddy",30,1256,501,2023)
print(user1.full_name())
print(user2.full_name())
print ("{} License status vaildation is: {}".format(user2.first_name,user2.is_valid_License()))
print ("{} License status vaildation is: {}".format(user1.first_name,user1.is_valid_License()))