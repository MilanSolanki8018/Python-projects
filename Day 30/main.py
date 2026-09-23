# python errors handling

try:
    file = open("file1.txt")
    dict = {"name": "rajesh"}
    print(dict["name"])
    # print(dict["mark"])
except FileNotFoundError:
    file = open("file1.txt", mode="w")
    file.write("File create successfuly")
except KeyError as error_mes:
    print(f"This {error_mes} key not found in dict.")
else:
    file = open("file1.txt")
    print(file.read())
finally:
    file.close()
    print("Every time excuted")


    list =[1,2]
    print(list[5])
