# Function with *args

# write a function that takes variable number of arguments and returns their sum.

def variable_args_sum(*args):
  # print("*args",*args)
  # print("args",args)
  # for a in args:
  #   print(a)

  return sum(args)


print(variable_args_sum(1,2,3,4))
print(variable_args_sum(1,2,3,4,5,6))
print(variable_args_sum(1,2,3,4,5,6,7,8))
