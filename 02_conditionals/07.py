coffee_size=input("Enter coffe size: ").upper()
extra_shot=False

if coffee_size not in ['SMALL','MEDIUM','LARGE']:
  print('Enter valid size')
  exit()

if extra_shot==True:
  print(coffee_size,"with extra shot")
else:
  print(coffee_size,"coffee")

