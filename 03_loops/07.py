# num = int(input("Enter num: "))

# while num<=1 or num>=10:
#   num = int(input("Enter num: "))


while True:
  num=int(input("Enter a number between 1 and 10: "))
  
  if 1<=num<=10:
    print("Thanks!")
    break
  else:
    print("Enter a valid number, try again ")

