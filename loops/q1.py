# count the positive numbers in a list

nums=[1,-2,3,-4,5,6,-3,2,4,-5];
count_positive=0;

for num in nums:
  if num>=0:
    count_positive+=1;

print(count_positive)
