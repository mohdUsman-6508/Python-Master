
even_num = [ x for x in range (1,10) if x%2==0]

# print(even_num)

list_mem_ref=iter(even_num)
print(list_mem_ref)

print(list_mem_ref.__next__())
print(list_mem_ref.__next__())
print(next(list_mem_ref))
print(list_mem_ref.__next__())
# print(list_mem_ref.__next__())

f=open('file.text')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
# print(f.__next__())
# print(f.__next__())

r= range(3)
print(r)
ri=iter(r)
print(ri)
print(next(ri))

for line in open('file.text'):
  print(line)