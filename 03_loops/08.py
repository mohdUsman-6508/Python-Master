import math

num = int(input("Check prime: "))
i=2

if num <=1:
  print("Not a prime number")
  exit()

while i<=math.sqrt(num):
  if num%i==0:
    print(str.format("{} is not a prime number",num))
    exit()
  i+=1;

print(str.format("{} is a prime number",num))
  
  
