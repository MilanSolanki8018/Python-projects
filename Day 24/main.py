"""file = open("first.txt", mode="r")
# print(file.write("first file practice"))
content = file.read()
print(content)
file.close()

# with use file not add close() automaticaly close file
with open("first.txt", mode="a") as file:
    file.write("\n use diffrent mode")
"""

# i am create new file in desktop and read this file file neame desk.txt using abosulute path
with open("C:\\Users\\Milan\\OneDrive\\Desktop\\desk.txt") as desk:
    print(desk.read())

# i am create new file in desktop and read this file file name first.txt using relative path
with open("./first.txt") as desk:
    print(desk.read())

