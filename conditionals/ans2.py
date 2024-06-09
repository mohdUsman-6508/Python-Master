age=int(input("Enter your Age: "))
day=input("Enter Day: ")

price=12;

if age<18:
  price=8

# Another way 
# price =12 if age>=18 else 8

if day=='Wednesday':
  price-=2

print("Ticket price: $",price)




