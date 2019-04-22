name=input("enter name:")
if name == "satya":
    print("hello satya")
    print("welcome to  world")
    print("\n")
class Chiru:
    def __init__(self,name,moviename):
        self.name = name
        self.moviename = moviename

    def info(self):
        print('nadigar:', self.name)
        print('padam:', self.moviename)
        print('\n')

telugu = Chiru("nani" , "jersey")
tamil  = Chiru("vijay sethupathi" , "96")
malayalam = Chiru("nivin", "premam")
kannada = Chiru("yash", "KGF")

telugu.info()
tamil.info()
malayalam.info()
kannada.info()
