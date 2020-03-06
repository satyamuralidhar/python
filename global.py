x = 10
z = 30
k = 20
def sample():
    y = 20
    print("y:",y)
    def new():
        global z
        z = z+1
        print("z:",z)
        def depart():
            global k 
            k = k+1
            print("k:",k)
        depart()
    new()
sample()
