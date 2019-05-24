# basic caluclator
# for addition , subtraction , multiply , division
def add(num1 , num2):
    return num1+num2
def subtract(num1 , num2):
    return num1-num2
def multiply(num1 , num2):
    return num1*num2
def divide(num1 , num2):
    return num1/num2
calculator = input("select from 1, 2, 3, 4 -:  " )

first = int(input("enter  first number: "))
second = int(input("enter second number: "))

if calculator == "1":
    print(add(first , second))
elif calculator == "2":
    print(subtract(first , second))
elif calculator == "3":
    print(multiply(first, second))
elif calculator == "4":
    print(divide(first, second))
else:
    print("error it's not possible please check select from")



