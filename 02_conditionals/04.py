color=input("Enter color: ").lower()
fruit='banana'
ripeness=''

if fruit.lower()=='banana':
    if color=='green':
      ripeness='unripe'
    elif color=='yellow':
      ripeness='ripe'
    elif color=='brown':
      ripeness='overripe'
    else:
      ripeness='do not eat'
else:
  print("No info")

if ripeness!='':
  print('Ripeness: ',ripeness)
  