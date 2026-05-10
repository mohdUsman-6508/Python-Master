import time

def timer(func):
      def wrapper(*args,**kwargs):
            start = time.time()
            result = func(*args,**kwargs)
            end = time.time()
            print(f"{func.__name__} executed in {end-start}sec")
            return result
      return wrapper

@timer
def example(n):
      time.sleep(n)
      print("Done!")
      
  
example(2)