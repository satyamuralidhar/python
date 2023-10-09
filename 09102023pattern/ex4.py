'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

num = 5

for row in range(num,0,-1):
    #o/p 54321
    for space in range(num-row+1):
        print(end=" ")
    for row in range(row): 
        #we are using row as a reverse order 
        print("*",end=" ")
    print()
       