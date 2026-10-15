'''
Take a decimal number as input (like 45.78) and output its:
- integer part (45)
- fractional part (.78)
'''


# Method 1
num = input("Enter the decimal number: ")
num_int, num_frac = num.split(".")

print(f"The integer part of the number {num} is {num_int} \n" 
      f"The fractional part of the number {num} is 0.{num_frac}")

# # Method 2
# num = float(input("Enter the decimal number: "))
# num_int = int(num)
# num_frac = abs(num) % 1

# print(f"The integer part of the number {num} is {num_int} \n" 
#       f"The fractional part of the number {num} is 0.{num_frac}")   #this is giving a strange fractional part because of floting-point precision issue