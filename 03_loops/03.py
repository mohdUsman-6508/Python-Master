
n=int(input("Enter n: "))

for i in range(1,11):
  if i==5:
    continue
  
  result_ith=i*n;
  print(str.format("{} * {} = {}",n,i,result_ith))
  