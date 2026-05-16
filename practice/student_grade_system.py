import json
import os


class Student:
    
    def __init__(self, name, roll_number,marks_list):
        self.name = name
        self.roll_number = roll_number
        self.marks_list = marks_list
        
    def calculate_average(self):
        average_marks = 0
        total_marks = 0
        total_subjects = len(self.marks_list)
        
        for marks in self.marks_list:
            total_marks+=marks
            
        average_marks = float(total_marks/total_subjects)
        return average_marks
    
    def display_report(self):
        print("*"*60)
        print(f" {self.name} {self.roll_number} {self.marks_list}")
        print("*"*60)
        
    
    
def load_students():
    try:
        if os.path.getsize('students.txt')>0:
            with open('students.txt','r') as file:
                data = json.load(file)
                # students = [Student(d['name'],d['roll_number'],d['marks_list']) for d in data]
                students = [Student(**d) for d in data]
                return students
        else:
            return []
    except FileNotFoundError:
        return []
    

def save(students):
    with open('students.txt','w') as file:
        json.dump([student.__dict__ for student in students],file,indent=4)
            

def find_topper(students):
    max_marks = 0
    temp_max_marks = 0
    topper_student = None
    
    for student in students:
        temp_max_marks = calc_total_marks(student.marks_list)
        if temp_max_marks > max_marks:
            max_marks = temp_max_marks
            topper_student = student
            
    print(f"Topper student: {topper_student.name} {topper_student.roll_number} {max_marks}")
    

def calc_total_marks(marks):
    total_marks=0
    for mark in marks:
        total_marks+=mark
    return total_marks


def search_student(students):
    roll_number = input("Enter roll number: ")
    
    for student in students:
        if student.roll_number == roll_number:
            student.display_report()
            return True
        
    print("Not found")
    return False


def add_student(students):
    name = input("Enter name: ")
    roll_number = input("Enter roll number: ")
    marks_list = []
    
    student = Student(name,roll_number,marks_list)
    students.append(student)
    return students


def add_marks(students):
    roll_number = input("Enter roll number: ")
    marks = int(input("Enter marks: "))
    
    for student in students:
        if student.roll_number==roll_number:
            student.marks_list.append(marks)
            break
        
    return students


def show_all_students(students):
    for student in students:
        student.display_report()
    
    
def main():
    print("Student Grade System | Choose an option")
    print("\n")
    students = load_students()
    while True:
        
        print("1. Add student")
        print("2. Add marks")
        print("3. Calculate average")
        print("4. Find topper")
        print("5. Search student")
        print("6. Show all students")
        print("7. Save")
        print("*"*60)
        
        choice = input("Enter choice: ")
        
        match choice:
            case "1":
                students=add_student(students)
                
            case "2":
               students = add_marks(students)
            
            case "3":
                roll_num = input("Enter roll number: ")
                for student in students:
                    if student.roll_number==roll_num:
                        avg = student.calculate_average()
                        print(avg)
                        break
                    
            case "4":
               find_topper(students)
            case "5":
                search_student(students)
                
            case "6":
                show_all_students(students)
        
            case "7":
                save(students)
                students = load_students()
            
            case _:
                print("Invalid choice")
                break
        

if __name__=="__main__":
    main()
    
	 