"""
2. Create a dictionary called school. Ask the user how many classes they want to enter. For each class, ask how many students are in that class.
  For each student, take details like name and age. Store the data in the format where the main dictionary has class names as keys, each class
  contains a sub-dictionary of students, and each student has their own dictionary of details like name and age.
"""

school = { }

classes = int(input("how many classes they want to enter :"))

for i in range(classes):
    class_name = input("Enter Class Name : ")

    student = int(input(f"how many students are in that class {class_name}: "))

    student_dict = {}

    for s in range(student):
        name = input(f"Enter name of student{s+1}:")
        age = str(input("Enter your age:"))
        roll_num = s+1
        student_dict[roll_num] = {
            "name" : name,
            "age" : age
        }

    school[class_name] = student_dict


print("School Dictionary :")
print(school)




