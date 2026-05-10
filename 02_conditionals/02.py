# movie ticket pricing based on age, >=18 --> 12$, else 8$, day="Wednesday" discount=2$

age= int(input("Enter age: "))
day= input("Enter day: ")

ticket_price=8
discount=0

if age>=18:
  ticket_price=12

if  day.upper()=='WEDNESDAY':
  discount=2;

ticket_price_with_discount=ticket_price-discount

print(str.format("Ticket price: ${}",ticket_price_with_discount))
