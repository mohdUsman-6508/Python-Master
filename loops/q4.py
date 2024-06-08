# reverse a string

str=input("enter a string:")

rev_str=""
j=-1;

for i in range(len(str)):
  rev_str+=str[j]
  j-=1

# alternative

# for ch in str:
#   rev_str=ch+rev_str
print(rev_str)
  




