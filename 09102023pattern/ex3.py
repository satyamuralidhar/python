'''
    *
   * * 
  * * * 
 * * * *
* * * * *

'''

num = 5
for row in range(0,num):# 0 , 1, 2, 3, 4
    for space in range(0,num-row-1):
        # 0 , 5-0-1 ==> 4spaces
        #curser will placed after 4th space 
        # col => row+1 => 0+1 => rnge => 0 "*" placed after 4th space
        #after print next row
        # 1 , 5-1-1 ==> 3spaces
        #curser will placed after 3th space
        #         # col => row+1 => 1+1 => rnge => 2 "*" placed after 3th space and 4th

        print(end=" ")
    for col in range(row+1):
        print("*",end=" ")
    print()