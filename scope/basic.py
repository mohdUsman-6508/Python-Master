
# scope 
# let's understand it with the help of an analogy

# let's say your whole village is a global level scope ,
# your home is local level scope,
# and different rooms in your home also have their own scope
# and you are living in a room inside your home
# let's say if you want to find a dog name 'Jaguar'
# then first you will find him in your room, if not found then in your home, then in your village 
# so you are searching your dog in local scope to global scope

# And it may be a case that in your village there may be another dog whose name is same as yours
# and there may be no relation between two.


# global level
x=100

# x in local variable exist so it fn will use local, if local does not exist then fn will search in global scope

def f1():
  # local x
  x=99
  print(x)

# f1()


# nothing found in local scope
# so global scope variable used
y=10

def f2():
  print(y)

# f2()


z=10

def f3(m):
  n=m+z
  print(n)

# f3(30)

# use it cautiously global

def f4():
  global x
  x=123
  print(x)

# f4()


# closure

def f5():
  x=1
  def f6():
    print(x)
  return f6


# here when we are returning the definition of the f6 to fn f5 then, we are returning the variable associated to it--> closure

# result=f5()
# print(result)
# result()


def coder(num):
  def programmer(x):
    return x**num
  return programmer

f=coder(2)
g=coder(3)


print(f(3))
print(g(4))


