
older_file = open('older.txt','w')

try:
  older_file.write('This is an older file, handle with care.')
finally:
  older_file.close()
  

# new way

with open('new_file.txt','w') as new_file:
  new_file.write("This a new file, you don't have to write finally and close the file manually.")