class ram:
    def __init__(self , name , domain):
        self.name = name
        self.domain = domain
    def dev(self):
        print("hi what is your name?", '\n', self.name)
    def ops(self):
        print("which domain you are working?", '\n', self.domain)
k = ram('satya', 'linux admin')
k.dev()
k.ops()

