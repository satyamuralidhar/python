class A():
    def MyData(self):
        print('this is mydata')
    def MyData4(self):
        print('this is mydata4')    
class B(A):
    def MyData2(self):
        self.MyData()
        self.MyData4()
        print('this is mydata2')
class C():
    def MyData3(self):
        print('this is mydata3')
x = A()
y = B()
z = C()
x.MyData()
y.MyData2()

#output:
#this is mydata
#this is mydata
#this is mydata4
#this is mydata2


##################

class A():
    def Ram(self):
        print("hi this is ram")
class B():
    def Sam(self):
        print("hi this is sam")
class C(A):
    def Lakshman(self):
        print("hi this is lakshman")
x = A()
y = B()
z = C()
x.Ram()
y.Sam()
z.Lakshman()
z.Ram()



#output:
#hi this is ram
#hi this is sam
#hi this is lakshman
#hi this is ram
