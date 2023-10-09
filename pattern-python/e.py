# *****
# *
# *****
# *
# *****

for row in range(5):
    for col in range(5):
        if row==0 or row==2 or row==4 or col==0:
            print("*",end="")
    print()
