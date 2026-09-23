# use *args
"""def add(*args):
    sums=0
    for i in args:
        sums += int(i)
    print(sums)

add(1,2,3,2,1,23)"""

# uae **kwargs
def calc(n,**kwargs):
    print(kwargs["add"])
    print(kwargs["sub"])

    n += kwargs["add"]
    print(n)
    n -= kwargs["sub"]
    print(n)

calc(10,add=5,sub=10)

print("\n \n")
class Student():
    def __init__(self,**kw):
        self.roll = kw.get("roll")
        self.name = kw["name"]
        self.marks = kw.get("mark")
#         using get() methode dictionary no find key an argument  return no error and direct key aacees return error
obj = Student(name="raj",mark=57)
print(obj.roll)
print(obj.name)
print(obj.marks)
