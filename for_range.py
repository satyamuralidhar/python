for i in range(100,104):
    print("assign value of i is :",i)
    for num in range(100,i):
        print(num,i)
        if num==102:
            pass

        
        
        
        
        
        
#2.Create the below pattern using nested for loop in Python.
        *  
        * *  
        * * *  
        * * * *  
        * * * * *  
        * * * * 
        * * * 
        * *  
        * 

        
number = int(input("enter the values: "))
for i in range(1,number+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for k in range(number-2,-1,-1):
    for m in range(k,-1,-1):
        print("*",end="")
    print()
        
        
        
      
 
 
