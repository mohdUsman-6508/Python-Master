
marks=int(input("Enter your number: "))
grade='E'

if marks>=101:
  print("Verify your marks")
  exit()


if marks<60:
  grade='F'
elif marks<70:
  grade='D'
elif marks<80:
  grade='C'
elif marks<90:
  grade='B'
else:
  grade='A'

print("Your grade is :",grade)

