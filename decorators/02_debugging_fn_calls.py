# def debug(func):
#   def wrapper(*args,**kwargs):
#     print(func.__name__)
#     for i in args:
#       print(i)
#     for k,v in kwargs.items():
#       print(k,v)
#   return wrapper

# alternative

def debug(func):
  def wrapper(*args,**kwargs):
    args_value=', '.join(str(arg) for arg in args)
    kwargs_value=', '.join(f"{k}={v}" for k,v in kwargs.items())

    print(f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
    return func(*args,**kwargs)
  
  return wrapper


@debug
def add(a,b,c):
  total_sum=a+b+c
  return total_sum

@debug
def greets(name,greet="salam"):
  print(f"{greet}! {name}")

s=add(1,2,3)
print(s)

greets("usman",greet="salam")