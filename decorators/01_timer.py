# create a decorator which caluculate the execution time of a functions


# fn inside fn and inside the inner function we called the passed fn

import time

def timer(func):
  def wrapper(*args,**kwargs):
    start=time.time()
    result=func(*args,**kwargs)
    end=time.time()
    print(f'{func.__name__} ran {end-start} sec')
    return result
  
  return wrapper


@timer
def say_hello():
  print("hello")

    


say_hello()


  
