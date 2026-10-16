'''
Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
- If salary < 30000 then 5%
- If salary is 30000 - 70000 then 15%
- If salary > 70000 then 25%
'''

salary = int(input("Please enter your salary: "))

tax_rate = 0
if salary < 30_000:
    tax_rate = 5
elif 30_000 <= salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

print(f"Your tax rate is {tax_rate}%, so your final tax will be {tax_rate*salary/100}")