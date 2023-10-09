# *   *
# ** **
# * * *
# *   *
# *   *

for row in range(5):
    for col in range(5):
        if (col==0) or (col==4) or ((row==col) and (col>0 and col<3)) or (row==1 and col==3):
            print("*",end="")
        else:
            print(end = " ")
    print()

