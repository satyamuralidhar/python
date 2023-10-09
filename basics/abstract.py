from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def disp(self):
        pass
    def disp2(self):
        pass 
class B(A):
    def disp(self):
        print("hi sai")
class C(B):
    def disp2(self):
        print("hi satya")
#b = B()
#b.disp()
c = C()
c.disp()
c.disp2()
