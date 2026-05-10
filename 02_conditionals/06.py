distance = float(input("Enter distance(Km): "))

if distance < 0:
  print("Enter valid distance")
  exit()
  
if distance <3:
  print("Walk")
elif distance <=15:
  print("Bike")
else:
  print("Car")












