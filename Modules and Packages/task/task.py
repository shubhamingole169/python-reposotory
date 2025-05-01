import json
import os


name = input("enter your name : ")
age = int(input("enter your age : "))
grade = list(map(int, input("Enter grades and seperate by space !!!").split()))



student = {
    "name": name,
    "age": age,
    "grade": grade
}


#step 1: Load existing data if the file exists

students = []

if os.path.exists("students.json"):
    with open("student.json", "r") as file:
        try:
            students = json.load(file)
        except json.JSONDecodeError:
            students = []

#step 2: Add new student

students.append(student)

#step 3: save all dat a back to file

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)
    
print("student saved !!!")


#step 4: print all Students

print("\n All Students: ")
for s in students:
    print(s)