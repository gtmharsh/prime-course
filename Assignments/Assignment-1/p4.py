'''
The user enters a string containing a number (e.g., "45"). Convert it to:
- an integer
- a float
- a string again
Print all three values with their types
'''

num = input("Enter a number: ")
int_num = int(num)
float_num = float(num)
str_num = str(num)

print(f"integer value of the {num} is {int_num} and type {type(int_num)}")
print(f"float value of the {num} is {float_num} and type {type(float_num)}")
print(f"string value of the {num} is {str_num} and type {type(str_num)}")
