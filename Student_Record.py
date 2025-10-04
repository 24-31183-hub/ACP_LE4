import os

doc = os.path.expanduser("~/Documents")
if not os.path.exists(doc):
    os.makedirs(doc)

display = """
==== Student Record Menu ====
1. Add Student
2. Open Student Record
3. Exit"""
def isdigit(s):
    for char in s:
        if char.isdigit():
            return True
    return False
while True:
    print("==== Student Record Management System ====")
    try:
        student_no = int(input("Student No: "))
    except ValueError:
        print("Invalid input. Please enter a valid student number.")
    try:
        student_name = str(input("Student Full Nam
        print("Invalid input. Please enter a valid name.")
    try:
        program = str(input("Program: "))
