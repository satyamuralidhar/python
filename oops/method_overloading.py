# if a mainly in the part of polymorphism


class overload:
    def poly(self,name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("enough")
obj = overload()
obj.poly()
obj.poly("Satya")
