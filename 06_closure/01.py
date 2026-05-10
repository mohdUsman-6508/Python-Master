
x=10

def f1():
  x=1
  print(x)
  
print(x)
f1()

def f2():
  print(x)
  
f2()

def f3():
  global x #not recommended
  x=100
  print(x)
  
print(x)
f3()
print(x)

def fun1(a):
  
  def fun2(b):
    return b**a
  
  return fun2

sq = fun1(2)
cu = fun1(3)

print(sq,cu)

print(sq(3))
print(cu(3))


def fun3():
  y=10
  def fun4():
    y=20
    print("Inside: ",y)
  fun4()
  print("Outside: ",y)
    
  
fun3()

def fun5():
  m=10
  n=20
  
  if m>0:
    n=30
    m=0
  print(f" m: {m}, n: {n}")

fun5()