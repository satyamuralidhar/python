'''
    * 
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''

def diamond(num):
    for i in range(num):
        print(' '*(num-i-1)+'* '*(i+1))
    for j in range(num,0,-1): #o/p 54321
        print(' '*(num-j+1)+'* '*(j-1))
diamond(5)