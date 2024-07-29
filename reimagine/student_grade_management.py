
students={
  "Issac":[9,8,10],
  "Tesla":[10,9,7],
  "Edison":[9,9,9]
}

print(f"\nUpdated list: {students}")

for student,grades in students.items():
  print(f'{student}:{grades}')

students["Einstein"]=[8,10,7]

for student,grades in students.items():
  avg_grades=sum(grades)/len(grades)
  print(f"Average grades of {student}: {avg_grades:.2f}")


# File handling

# writing to a file 
with open("students.txt","w") as file:
  for student,grades in students.items():
    file.write(f"{student}:{grades} \n")

# reading from a file
with open("students.txt","r") as file:
  content=file.read()
  print("Content:\n")
  print(f"{content}")
  
