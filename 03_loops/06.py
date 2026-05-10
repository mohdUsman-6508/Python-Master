num = int(input("Enter num: "))
temp=num

factorial=1;

if num==0:
  print(str.format("Factorial of the {} is {}",num,factorial))
  exit()
  
while temp>0:
  factorial*=temp
  temp-=1
  
print(str.format("Factorial of the {} : {}",num,factorial))