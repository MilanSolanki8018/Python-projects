# with open("weather_data.csv") as data:
#     list_out_data = data.readlines()
#     print(list_out_data)

"""import csv

with open("weather_data.csv") as data:
   list_out_data = csv.reader(data)
   temperatures = []
   day = []

   for row in list_out_data:
       print(row)

       #print only temperatures

       if row[1] != "temp":
           temperatures.append(int(row[1]))
       if row[0] != "day":
           day.append(row[0])

   print(f"Days {day}")
   print(f"temperatures {temperatures}")"""

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(f"\n {data["temp"]}")