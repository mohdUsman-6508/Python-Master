
file=open('error.txt','w')

try:
  file.write("This is the traditional way of handling file, nowadays we use 'with' ")
finally:
  file.close()

with open('new_way.txt','w') as file:
  file.write("Yes this is the new way")

