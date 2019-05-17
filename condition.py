#AND

passport = True
visa = False

if passport and visa:
    print('Eligible for going abroad')
else:
    print("Not Eligible for going abroad")
    
#OR

passport = True
visa = False

if passport or visa:
    print('Eligible for applying visa')
else:
    print('Not Eligible for visa')
  
#NOT

passport = True
police_case = False

if passport and not police_case:
    print('Eligible for applying passport')
else:
    print("Not Eligible for applying passport")
