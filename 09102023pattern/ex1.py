'''
*
* *
* * *
* * * *
* * * * *

'''

for row in range(5): # 0 , 1, 2, 3 ,4 , 5
    for col in range(row + 1): # (0+1) (1+1) (2+1)....
        print("*",end=" ")
    print() 

'''
iter 1: 
=======
row => 0 
col => 0 + 1 => 1
then col range(1) = 0
print "*" at 0th position

* _ ('curser will move to one step after "*"')
it will go nxt line using print()

iter 2: 
======
row => 1
col => 1+1 => 2
col range(2) => 0,1
we got two values col will iter 2 times
print "*" at 0th position {0 value is done}
next curse will move to one position 
print "*" at 1th position {1 value is done}
* _ ('curser will move to one step after "*"')
it will go nxt line using print()

iter 3: 
======
row => 2
col => 2+1 => 3
col range(3) => 0,1,2
we got two values col will iter 3 times
print "*" at 0th position {0 value is done}
next curse will move to one position 
print "*" at 1th position {1 value is done}
* _ ('curser will move to one step after "*"')
print "*" at 2th position {2 value is done}
* _ ('curser will move to one step after "*"')
next curse will move to one position
it will go nxt line using print()

iter 4: 
======
row => 3
col => 3+1 => 4
col range(4) => 0,1,2,3
we got two values col will iter 4 times
print "*" at 0th position {0 value is done}
next curse will move to one position 
print "*" at 1th position {1 value is done}
* _ ('curser will move to one step after "*"')
print "*" at 2th position {2 value is done}
* _ ('curser will move to one step after "*"')
print "*" at 3th position {3 value is done}
next curse will move to one position
it will go nxt line using print()



'''