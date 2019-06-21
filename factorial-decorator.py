import time
import math
def timestamp(func):
    def calc(*args , **kwargs):
        begin = time.time()
        func(*args , **kwargs)
        end = time.time()
        sum = end - begin
        print('time taken :' , func.__name__ , sum)
    return calc
@timestamp
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
num = 20
factorial(num)

#output:
# 2432902008176640000
# time taken : factorial 2.015599250793457

