class Ram():
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def sample(self):
        print('name: ' , self.name)
        print('age: ' , self.age)
class Lakshman():
    def __init__(self , bike , technology ):
        self.bike = bike
        self.technology = technology
    def demo(self):
        print('bike: ' , self.bike)
        print('technology: ' , self.technology)
class Mohan(Lakshman):
    def __init__(self , book , laptop ):
        self.book = book
        self.laptop = laptop
    def city(self):
        print('book: ' , self.book)
        print('laptop: ' , self.laptop)
aim = Ram("pavan" , "21")
aim.sample()
person = Lakshman("ns200" , "BS4")
person.demo()
vizag = Mohan("cheguvera" , "Dell")
vizag.city()
