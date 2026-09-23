import csv

import pandas

"""data = pandas.read_csv("weather_data.csv")
print(data)

temp_list = data["temp"].to_list()
print(temp_list)

# print(f"Average temp {round(sum(temp_list) / len(temp_list),2)}")
#using pandas
print(f"Average temp {data["temp"].mean()}")
print(f"Max temp {data["temp"].max()} \n")

# print max data coloum
print(data[data.temp == data.temp.max()])

# print sunday condition
sunday = data[data.day == "Sunday"]
print(sunday.condition)"""

# using datafream

dictonary = {
    "student": ["meet","rahul","kepel"],
    "marks": [56,78,34]
}

data = pandas.DataFrame(dictonary)
print(data)
data.to_csv("student_data.csv")