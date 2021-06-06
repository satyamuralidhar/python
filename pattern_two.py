# *****
# *****
#    **
#    **
# *****
# *****
# **
# **
# *****
# *****





for row in range(10):
    for col in range(5):
        if (row==0 or row==1):
            print("*",end="")
        elif (row==8 or row==9):
            print("*",end="")
        elif (row==2 and col==3) or (row==2 and col==4):
            print("*",end="")
        elif (row==3 and col==3) or (row==3 and col==4):
            print("*",end="")
        elif (row==4):
            print("*",end="")
        elif (row==5):
            print("*",end="")
        elif (row==6 and col==0) or (row==6 and col==1):
            print("*",end="")
        elif (row==7 and col==0) or (row==7 and col==1):
            print("*",end="")
        elif (row==2 and col==0) or (row==2 and col==1) or (row==2 and col==2) or (row==3 and col==0) or (row==3 and col==1) or (row==3 and col==2) :
            print(" ",end="")
        elif (row==5 and col==2) or (row==5 and col==3) or (row==5 and col==4)  or (row==6 and col==2) or (row==6 and col==3) or (row==6 and col==4):
            print(" ",end="")
    print()
