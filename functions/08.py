# Function with **kwargs

# create a function that accepts any number of keyword arguments and prints them in the format key:value


# def print_kwargs(name,power):
#   print("Name:",name,"Power:",power)

# print_kwargs(name="superman",power="laser")
# print_kwargs(power="ultra instinct",name="goku")


def print_kwargs(**kwargs):
  for k,v in kwargs.items():
    print(f'{k}:{v}')
  

print_kwargs(name="superman",power="laser")
print_kwargs(name="goku",power="ultra instinct",enemy='frieza')