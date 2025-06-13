"""
1. Nested List Program Instruction (as a string):
	Create a program that takes a number input from the user. Based on this number (e.g., 20), take that many inputs from the user. Then, sort the inputs into four separate sublists:
	One for odd numbers
	One for even numbers
	One for alphabets (letters)
	One for special characters
	These four sublists should be stored inside one main list (a nested list). Finally, print each sublist from the main list one by one.

"""

odd_list = []
even_list = []
alphabet_list = []
special_list = []
# f=[]
number = int(input("Enter a Number: "))
for i in range(number):
    value = input(f"Enter Value {i+1} :")
    # f.append(value)
    if value.isdigit():
        value = int(value)
        if value % 2 == 0:
            even_list.append(value)
        else:
            odd_list.append(value)
    elif value.isalpha():
        alphabet_list.append(value)
    else:
        special_list.append(value)

print(odd_list)
print(even_list)
print(alphabet_list)
print(special_list)
# print(f)
nested_list = [odd_list,even_list,alphabet_list,special_list]
print(nested_list)
