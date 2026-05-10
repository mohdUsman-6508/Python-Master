
def cart(*args):
  print(args)
  print(type(args))
 
  
  for i in args:
    print(i)
  
  return sum(args)

print(cart(1,2,3,4,5))
