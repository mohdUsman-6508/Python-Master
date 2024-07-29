
# DECORATORS @  

def debug(func):
  def wrapper(*args,**kwargs):
    result=func(*args,**kwargs)
    print(f"{func.__name__}({args},{kwargs} {result})")
    return result
  return wrapper

@debug
def add(a,b):
  return a+b

@debug
def mul(a,b):
  return a*b

add(2,4)
mul(6,3)

# Generators

def fibbonacci(n):
  a,b=0,1
  while a<n:
    yield a
    a,b=b,a+b

for num in fibbonacci(10):
  print(num)



# Context Managers

class FileHandler:
  def __init__(self,filename,mode):
    self.filename=filename
    self.mode=mode

  def __enter__(self):
    self.file=open(self.filename,self.mode)
    return self.file
  
  def __exit__(self,exc_type,exc_val,exc_tb):
    self.file.close()

  
with FileHandler("Example.txt","w") as file:
  file.write("Hello, World!")
