'''
Let's create a “Number Guessing Game”.  Given a secret number (already 
decided by you), write a program that asks the user to guess it and prints:
• "Too high" if the guess is above the number
• "Too low" if the guess is below
• "Correct!" if the guess matche
'''

import random

def guess_num(n):
    while True:
        guess = int(input("What's your guess?\n"))
        if guess > n:
            print("Too high")
        elif guess < n:
            print("Too low")
        else:
            print("Correct")
            break

if __name__ == "__main__":
    n = random.randint(1, 100)
    print("Welcome to the 'Number Guessing Game'\nYou're supposed to guess a number between 1 and 100 (both inclusive)")
    guess_num(n)