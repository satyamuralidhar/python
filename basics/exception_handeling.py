

a = 8
b = 2

try:
    print("resource is opened")
    print(a/b)
    h = int(input("enter a number:  "))
    print(h)
except Exception as e:
    print("you cannot devided by number using zero" , e)
except ZeroDivisionError as g:
    print("its can't devided by zero" , g)
except ValueError as k:
    print("value type error")
finally:
    print("resource is closed")
