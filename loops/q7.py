# validate input

num=int(input("Enter a number: "))

while True:
  if num in range(1,10):
    num=int(input("enter a number:"))
  else:
    print("exit:")
    break
    

