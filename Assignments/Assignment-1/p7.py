'''
Ask the user for a temperature in Celsius (string input). 
Convert it to float, then calculate and print temperature in Fahrenheit.
Conversion Formula:
Fahrenheit = (Celsius * (9/5)) + 32
'''

C_temp = int(input("Enter Temperature in Celsius: "))
C_temp = float(C_temp)

F_temp = (C_temp * (9/5)) + 32
print(f"The Fahrenhite value of the temperature {C_temp} celsius is {F_temp:.2f}")