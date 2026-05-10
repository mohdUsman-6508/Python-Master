marks=int(input("Enter marks: "))

if marks<0 or marks>100:
  print('Enter valid marks')
  exit()

grade=''

if marks >= 90:
  grade='A'
elif marks >= 80:
  grade='B'
elif marks >= 70:
  grade='C'
elif marks >= 60:
  grade='D'
else:
  grade='F'
  
print("Your grade is: ",grade)


