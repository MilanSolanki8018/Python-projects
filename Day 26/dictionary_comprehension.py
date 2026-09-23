import random
import pandas

name = ["vivek","manan","vipul","meet","raj"]

student_score = {new_key:random.randint(1,100) for new_key in name}
print(student_score)

passed_student = {key:val for (key,val) in student_score.items() if val > 33 }
print(passed_student)

student = {"student" : ["vivek","manan","vipul","meet","raj"],
           "marks": [25,67,84,23,45]}


student_dataframe = pandas.DataFrame(student)
print(student_dataframe)

for (key,val) in student_dataframe.iterrows():
    print(val)