'''
Design a program to continuously input a number n from user & print if it is positive or negative until the user enters "Quit".
'''


if __name__ == "__main__":
    while True:
        n = input("Enter a number or 'Quit' to exit:\n")
        if n.lower() == "quit":
            break

        try:
            n = int(n)
        except ValueError:
            print("Invalid input! Please enter an integer.\n")
            continue
        
        if int(n) > 0:
            print("The number you entered is positive.\n")
        elif int(n) < 0:
            print("The number you entered is negative.\n")
        else:
            print("The number you entered is zero.\n")