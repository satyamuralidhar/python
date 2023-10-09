birthday = input('Enter birth year: ')
current_age = 2019 - int(birthday)
print(current_age)
if current_age > 18:
    print('hey you are major')
else:
    print('sorry you are minor')
