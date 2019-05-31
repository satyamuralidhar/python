def Ram(func):
    def inside(a,b):
        if b == 0:
            print("b is a zero digit not possible")
        elif a ==0:
            print("a is a zero digit not possible")
        else:
            print("get solved")
        return
        func(a , b)
    return inside

@Ram
def div(a , b):

    return a/b
#div = Ram(div)
print(div(10 , 0))
