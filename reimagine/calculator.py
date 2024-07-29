 
def add(num1,num2):
  return num1+num2

def sub(num1,num2):
  return num1-num2

def mul(num1,num2):
  return num1*num2

def div(num1,num2):
  if num2==0:
    return 0;
  else:
    return num1/num2
  

  
print("____________________________________")
print("+-*/+-*/+-*/ 🧮CALCULATOR🧮 /*-+/*-+/*-+  ")
print("------------------------------------")

print("Enter two numbers:")
while True:
  num1=int(input("Number1:"))
  num2=int(input("Number2:"))
  operator=input("""Select an operation( +,-,*,/) to perform:""")
  result=0;
  if(operator=="0"):
    break

  if operator=="+":
    result=add(num1,num2)
  elif operator=="-":
    result=sub(num1,num2)
  elif operator=="*":
    result=mul(num1,num2)
  elif operator=="/":
    result=div(num1,num2)
    if result==0:
      print("Not defined")
      break
  else:
    print("Choose a valid operator.")
    continue

  print(f"""{num1} {operator} {num2} = {result}""")

  yesOrNo=input("Do you want to calculate more(y/n):")
  if yesOrNo=="n":
    print("""    ____________________________________
    Thanks for using our application 🤓
    ------------------------------------""")
    break
  else:
    continue
  

  




