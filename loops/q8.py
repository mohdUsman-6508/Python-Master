# prime number checker

num=int(input("Enter a number: "))

if num==1 or num<=0:
  print(f'{num} is not a prime number.')
  exit()

for i in range(2,num):
  if num%i==0:
    print(f'{num} is not a prime number.')
    exit()
  

print(f'{num} is a prime number')

