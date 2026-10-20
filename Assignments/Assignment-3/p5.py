'''
Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key ('A', 'B', 'C,' 'D') 
depending on the operation they want to perform on the dictionary:
1) A - Add a student
2) B - Update marks
3) C - Search for a student
4) D - Display all students and marks
'''

import time

def add_student(D, name, marks):
    D[name] = marks

def update_marks(D, name, marks):
    D[name] = marks

def search_student(D, name):
    if name in D:
        return True
    else:
        return False

def show_details(D, name):
     print(f"{name} has {D[name]} marks")

def display_all(D):
    print("Please find below the list of students and their respective marks:")
    for name in D:
        print(f"{name} has {D[name]} marks")


if __name__ == "__main__":
    D = {"NoOne": 100, "Sanjana": 97, "Harsh": 97, "Rahul": 95, "Anjali": 96}
    while True:

        choice = input(f"\nPlease select an option below:\n"
              f"A - Add a student\n"
              f"B - Update marks for a student\n"
              f"C - Search for a student\n"
              f"D - Display all students and their marks\n"
              f"E - Exit\n")

        if choice.lower() == 'a':
            name = input("\nPlease enter the student name: ")
            if search_student(D, name):
                print(f"{name} already exists")
                show_details(D, name)
            else:
                marks = int(input(f"\nPlease enter {name} marks: "))
                add_student(D, name, marks)
        elif choice.lower() == 'b':
                    name = input("\nPlease enter the student name: ")
                    if search_student(D, name):
                        show_details(D, name)
                        marks = int(input(f"Please enter updated marks for {name}: "))
                        update_marks(D, name, marks)
                    else:
                         print(f"No student with name {name} exists")
        elif choice.lower() == 'c':
            name = input("\nPlease enter the name of the student you wish to search for: ")
            if search_student(D, name):
                show_details(D, name)
            else:
                 print(f"No student named {name} exist")
        elif choice.lower() == 'd':
             display_all(D)
        elif choice.lower() == 'e':
             break
        else:
             print("\nPlease enter a valid input...\n")
        time.sleep(1)