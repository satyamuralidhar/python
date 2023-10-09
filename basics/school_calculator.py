def add(telugu , english , hindi , maths , science, social):
    return telugu+english+hindi+maths+science+social
telugu = int(input("enter telugu marks:- "))
english = int(input("enter english marks:- "))
hindi = int(input("enter hindi marks:- "))
maths = int(input("enter maths marks:- "))
science = int(input("enter science marks:- "))
social = int(input("enter social marks:- "))
total =  telugu+english+hindi+maths+science+social

per = float(total)*(100/600)
print("Percentage is: ",per  )
if per >= 70:
    print("A Grade")
elif per >= 60:
    print("B grade")
elif per >= 50:
    print("C Grade")
else:
    print("D Grade")


