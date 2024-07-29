
def safe_divide(a,b):
  try:
    return a/b
  except ZeroDivisionError as e:
    return str(e)
  finally:
    print(":)")
  

num1=float(input("Number1:"))
num2=float(input("Nubmer2:"))

result=safe_divide(num1,num2)

print(f"Result:{result}")
