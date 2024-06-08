# check uniqueness of a list

fruits=['lichi','mango','orange','apple','banana','apple']

for fruit in fruits:
  i=0
  for fruit_in in fruits:
    if fruit==fruit_in:
      i+=1
      if i>=2:
         print(fruit)
         exit()
      


