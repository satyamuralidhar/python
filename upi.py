upi = 12345
entry_count = 0
entry_limit = 1
while entry_limit > entry_count:
    encrypt = int(input('password: '))
    entry_count += 1
if encrypt == upi:
    print('you won the 100 rupees')
else:
    print('better luck next time')
