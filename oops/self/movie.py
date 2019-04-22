class Chiru:
    def __init__(self,name,moviename):
        self.name = name
        self.moviename = moviename

    def info(self):
        print('nadigar:', self.name)
        print('padam:', self.moviename)

telugu = Chiru("nani" , "jersey")
tamil  = Chiru("vijay sethupathi" , "96")
malayalam = Chiru("nvivin", "premam")
kannada = Chiru("yash", "KGF")

telugu.info()
tamil.info()
malayalam.info()
kannada.info()
