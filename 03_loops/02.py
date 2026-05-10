n=2;
sum_of_even_nums=0;

for i in range(n+1):
  if i%2==0:
    sum_of_even_nums+=i
    
print(str.format('Sum of even number upto {} is {}',n,sum_of_even_nums))
