pet = input("Enter pet species: ").lower()
age = int(input("Enter pet age: "))

if pet=='dog' and age<2:
  print("puppy food")
elif pet=='cat' and age>5:
  print("senior cat food")
else:
  print("simple food")
  