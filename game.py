class sam:
     def __init__(self , game , version):
         self.game = game
         self.version = version
     def insta(self):
         print("enter name: " , self.game)
         print(" enter version :", self.version)
web = sam("gta" , "v12")
web2 = sam("pubg" , "v2")
web.insta()
web2.insta()
