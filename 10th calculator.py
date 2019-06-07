# 10th calclator
def add(TeluguPaper1 , TeluguPaper2 , EnglishPaper1 , EnglishPaper2 , Hindi , MathematicsPaper1 , MathematicsPaper2 ,Physics , NS , SocialPaper1 , SocialPaper2):
    return TeluguPaper1 + TeluguPaper2 + EnglishPaper1 + EnglishPaper2 + Hindi + MathematicsPaper1 + MathematicsPaper2 +Physics + NS + SocialPaper1 + SocialPaper2
TeluguPaper1 = int(input("Enter TeluguPaper1 marks: "))
TeluguPaper2 = int(input("Enter TeluguPaper2 marks: "))
EnglishPaper1 = int(input("Enter EnglishPaper1 marks: "))
EnglishPaper2 = int(input("Enter EnglishPaper2 marks: "))
Hindi         = int(input("Enter Hindi marks: "))
MathematicsPaper1 = int(input("Enter MathematicsPaper1 marks: "))
MathematicsPaper2 = int(input("Enter MathematicsPaper2 marks: "))
Physics = int(input("Enter Physics marks: "))
NS = int(input("Enter NS marks: "))
SocialPaper1 = int(input("Enter SocialPaper1 marks: "))
SocialPaper2 = int(input("Enter SocialPaper2 marks: "))
total = TeluguPaper1 + TeluguPaper2 + EnglishPaper1 + EnglishPaper2 + Hindi + MathematicsPaper1 + MathematicsPaper2 + Physics + NS + SocialPaper1 + SocialPaper2
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
