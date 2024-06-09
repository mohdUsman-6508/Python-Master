# Recursive Function
# Create a recursive function to calculate the factorial of a number

def fact(n):
  if n==0:
    return 1
  
  fact_nm1=fact(n-1)
  return n*fact_nm1

print(fact(5))
