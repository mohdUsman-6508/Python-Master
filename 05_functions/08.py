
def print_kwargs(**kwargs):
  print(*kwargs)
  
  for k,v in kwargs.items():
    print(f"{k}:{v}")
  

print_kwargs(name="hero", power="power")
print_kwargs(name="cat")
print_kwargs(power="cute",color="white")