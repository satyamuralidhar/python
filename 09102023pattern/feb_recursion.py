def feb(i):
    if i==0:
        return 0
    elif i==1:
        return 1
    else:
        return (feb(i-2)+feb(i-1)) #==> 2-2+2-1 => 0+1 => 1 => 3-2+3-1

febinocci = []
user_input = int(input("Enter Value: "))

if user_input < 0:
    print("Please Enter NonZero value")
else:

    for result in range(user_input):
        print(feb(result))
        febinocci.append(feb(result))

print(febinocci)

