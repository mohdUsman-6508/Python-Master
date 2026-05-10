import time

def cache(func):
    cached_value={}
    def wrapper(*args,**kwargs):
        print(cached_value)
        if args in cached_value:
            return cached_value[args]
        result = func(*args,**kwargs)
        cached_value[args] = result
        return result
    return wrapper


@cache
def long_running_func(a,b):
  time.sleep(4)
  return a+b


print(long_running_func(2,3))
print(long_running_func(2,3))