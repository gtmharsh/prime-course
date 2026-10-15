'''
Ask the user for: Principal(P), Rate(R), Time(T). 
Convert all to float and compute simple interest:
SI = (P * R * T)/100
'''

P = float(input("Enter Principal amount: "))
R = float(input("Enter interest rate: "))
T = float(input("Enter time in years: "))

SI = (P * R * T)/100

print(f"Simple Interest for the Principal {P} "
      f"for {T} years at an interest rate of {R}% "
        f"is {SI:.2f}")