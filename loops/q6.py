# factorial calculator

# hence proved that python is a number strong language

num=int(input("Enter a num:"))
fact=1

if num<0:
  print("enter a valid number.")
  exit()

# for i in range(1,num+1):
#   fact*=i

# alternative

while num>0:
  fact*=num
  num-=1

print("factorial:",fact)
