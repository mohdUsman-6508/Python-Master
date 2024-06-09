
color=input("Enter the color of the fruit: ")
fruit=input("Enter the fruit name: ")

if fruit=='banana' or fruit=='mango':
  if color=='green':
    print("This banana is not ready to eat yet")
  elif color=='yellow':
    print("This banana is ready to eat")
  else:
    print("This banana is not good to eat")
elif fruit=='apple' or fruit=='papaya':
  if color =='green':
    print("This fruit is not ready to eat.")
  elif color=='red':
    print("This fruit is ready to eat.")
  else:
    print("This fruit is not ready to eat.")
else:
  print("You can eat !")







