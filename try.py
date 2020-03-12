#example 1:

try:
    num = int(input("enter a number: "))
    print(10/num)
    for x in range(10):
        if x==2:
            break
except ArithmeticError as e:
    print("error is got",e)
else:
    print("no exception in try block")

#example 2:

try:
    num = int(input("enter a number: "))
    print(10/num)
    for x in range(5):
        if x==2:
            break
except ZeroDivisionError as e:
    print("error is got: ",e)
else:
    print("Done")

# example 3:

try:
    num = int(input("enter a number: "))
    print(10/num)
    print(10 + "satya")
except ZeroDivisionError as a:
    print(a)
except ValueError as b:
    print(b , "Value Error")
except TypeError as c:
    print(c)
else:
    print("Done")

# example 4:
try:
    print("new")
    n = int(input("enter number: "))
    try:
        print(10/n)
        print(10 + "satya")
    except ValueError as a:
        print("10/n as vaule error: ",a)
    except TypeError as b:
        print("10 + satya as type error: ",b)
except ZeroDivisionError as end:
    print("n as zero division error: " , end)
else:
    print("done")
    
