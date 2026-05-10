
list = ['apple','mango','banana','pomegranate','grape','banana']


for i in range (0,len(list)):
  for j in range (i+1,len(list)):
    if list[i]==list[j]:
      print("First Duplicate found: ",list[i])
      exit()
    j+=1
  i+=1
  
print("No duplicate list item found")
