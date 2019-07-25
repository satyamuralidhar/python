class ram:
    def __init__(self , name , domain):
        self.name = name
        self.domain = domain
    def dev(self):
        print("hi what is your name?", '\n', self.name)
    def ops(self):
        print("which domain you are working?", '\n', self.domain)
class sam:
    def __init__(self , age):
        self.age = age
    def safe(self):
        print("age is ", self.age)
i = sam(9.5)
i.safe()
print('\n')
k = ram('satya', 'linux admin')
k.dev()
k.ops()
print('\n')
class sahu:
    def __init__(self , teach , earn):
        self.teach = teach
        self.earn = earn
    def jhonny(self):
        print('he is teaching : ' , self.teach)
        print('earning :', self.earn)
j = sahu('english' , '15k')
j.jhonny()
