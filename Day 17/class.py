class student:
    def __init__(self,id,name):
        print("Constructor attribute using asign ")
        self.id = id
        self.name = name

    def result(self,marks):
        print("object method")
        self.marks = marks
        print(marks)


obj = student(121,"meet")
print(obj.id)
print(obj.name)
obj.result(55)

