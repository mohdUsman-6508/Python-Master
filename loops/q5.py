# find the first non-repeated character

char_list=['a','b','c','a','b','c','e','d','c']

ans=""

for ch in char_list:
  i=0
  for ch1 in char_list:
    if ch==ch1:
      i+=1
      if i>=2:
        break
  
  if i==1:
    ans=ch
    break

print(ans)
      