'''
       *
      * * 
    * * * *
  * * * * * *
    * * * *
      * * 
       * 
'''

#adding pyramid with front and reverse order
# 
#  

#front pyramid
'''

    *
   * * 
  * * * 
 * * * *
* * * * *

'''
num = 7

for row in range(0,num): #0,1,2,3,4,5,6
    for space in range(num-row-1):
    # 7-0-1 => 6 => 0 1 2 3 4 5
    # 7-1-1 => 5 => 0,1,2,3,4
        print(end=" ")
    for col in range(row+1):
        # 0+1 => 1
        # 0+2 => 2 => 0,1 => 2*s
        print("*",end=" ")
    print()

# reverse pyramid
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''

print(f"\n")
print("-------------")
print(f"\n")

num = 7

for row in range(num,0,-1):
    for space in range(num-row+1):
        #7-7+1 => 1=> 0 => 0 space
        #7-6+1 => 2=> 0,1 => 1 space
        #7-5+1 => 3=> 0,1,2 => 2 space
        print(end=" ")
    for col in range(row):
        print("*",end=" ")
    print()



#refer above for diamond shape

num=7
for i in range(num):
    print(' '*(num-i-1)+'* '*(i+1))
for j in range(num,0,-1): #o/p 54321
    print(' '*(num-j+1)+'* '*(j-1))
    #5-
    '''
    spaces:               
    5-0-1 => 4 
    5-1-1 => 3
    col:
     0+1 => 1 => 0 * 
     1+1 => 2  => 0,1 => 2* 
     2+1 => 3 => 0,1,2 => 3*

    space: for revers order
    5-0+1 => 6 => 012345
    5-1+1 => 5 => 01234
    5-2+1 => 4 => 0123

    

    '''



