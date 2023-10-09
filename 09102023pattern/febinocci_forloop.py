# 0 1 1 2 3 5 8 13
'''
0 1 = 1
  1 1 = 2
     1 2 = 3
        2 3 = 5
          3 5 = 8
             5 8 = 13
               8 13 = 21
'''

first_number = 0
second_number = 1
result = 0



user_input = int(input("Enter Input Value: "))

print(first_number)
print(second_number)
for feb in range(0,user_input):
    result = first_number + second_number #==> result = 0 + 1 = > 1
    first_number = second_number # ==> first_number = 1
    second_number = result
    print(result)
