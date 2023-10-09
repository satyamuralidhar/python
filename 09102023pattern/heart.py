'''
    * *  * * 
   *    *    *
    *       * 
      *    *
         * 
'''

rows = 6
cols = 7

for row in range(rows):
    for col in range(cols):
        if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
            print("*",end="")
        else:
            print("",end=" ")
    print()