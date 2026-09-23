#List Comprehension


number = [1,2,3,4]
new = [i+1 for i in number]
print(new)

# string
name = "solanki"
new_list = [l for l in name]
print(new_list)

double = [i * 2 for i in range(1,6)]
print(double)

name = ["vivek","manan","vipul","meet","raj"]
short_name = [n.upper() for n in name if len(n) > 4]
print(short_name)