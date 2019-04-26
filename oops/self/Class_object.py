class Avengers:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def eating(self , food):
        self.food = food
        return "{} is eating {}".format(self.name , self.food)
    def planting(self , tree):
        self.tree = tree
        return "{} is plannting {}".format(self.name , self.tree)

vijay = Avengers("vijay" , 27)
mani = Avengers("main" , 27)
print("age of {} is {}".format(vijay.name , vijay.age))
print(vijay.eating("biryani"))
print("\n")
print("age of {} is {}".format(mani.name , mani.age))
print(mani.planting("a mango tree"))

