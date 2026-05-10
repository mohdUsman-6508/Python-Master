password = input("Check password strength: ")

pass_len=len(password)

if pass_len<6:
  print("Weak")
elif pass_len<=10:
  print("Medium")
elif pass_len>10:
  print("Strong")
