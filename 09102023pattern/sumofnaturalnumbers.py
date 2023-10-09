#natural numbers 1 2 3 4 5 6 7 8 9 0 

#sum of natural number n(n+1)/2

def SumOfNaturalNum(val):
    result = val*(val+1)
    result = result/2
    return result

user_input= int(input("Enter Value: "))
if user_input > 0:
    print(SumOfNaturalNum(user_input))
else:
    print("Please Enter NonZero or -ve Value")