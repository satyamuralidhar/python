#febinocci series
n1,n2 = 0,1 
count = 0
nterm = int(input("enter the input value : " ))
if nterm<=0:
    print("enter the value is greater than Zero ")
elif nterm>=1:
    while count < nterm:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
        
    
