# Import necessary modules
import os

# Ensure the Documents directory exists
doc = os.path.expanduser("~/Documents")
if not os.path.exists(doc):
    os.makedirs(doc)

# Menu display string
display = """
==== Student Record Menu ====
1. Add Student
2. Open Student Record
3. Exit"""

# Validation functions for numbers
def numbers(s):
    for i in s:
        if i in "0123456789":
            return True
    return False

# Main loop for user interaction
while True:
    print(display)
    try:
        choice = int(input("Enter your choice: "))
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    # Handle user choices
    if choice == 1:
        while True:
            print("\n===== Add Student Record =====\n")
            try:


                # Student number
                student_no = input("Student No: ").strip()
                if not student_no.isdigit():
                    raise ValueError("Please enter a valid student number.\n")
                
                # Full name
                student_name = input("Full Name: ").strip()
                if numbers(student_name) or not student_name:
                    raise ValueError("Name cannot be empty and should not contain numbers.\n")
                
                # Program
                program = input("Program: ").strip()
                if not program:
                    raise ValueError("Program cannot be empty.\n")
                
                # Age
                age = input("Age: ").strip()
                if not numbers(age) or not age:
                    raise ValueError("Age cannot be empty and must contain only numbers.\n")
                elif int(age) <= 0:
                    raise ValueError("Age must not be zero or negative.\n")

                # Gender
                gender = input("Gender: ").strip().upper()
                if gender not in ["MALE", "FEMALE", "M", "F"]:
                    raise ValueError("Gender must be Male (M) or Female (F).\n")
                
                # Birthday
                birthday = input("Birthday: ").strip()
                if not birthday:
                    raise ValueError("Birthday cannot be empty.\n")
                
                # Contact number
                contact = input("Contact No: ").strip()
                if not numbers(contact) or not contact:
                    raise ValueError("Contact number cannot be empty and must contain only numbers.\n")
                

                # convert and save to file
                student_no = str(student_no)
                student_name = list(student_name.split())
                program = str(program)
                age = int(age)
                gender = str(gender)
                if gender == "M":
                    gender = "MALE"
                elif gender == "F":
                    gender = "FEMALE"
                birthday = str(birthday)
                contact = str(contact)


                # create and write to file
                number_id = "student_" + student_no + ".txt"
                file_path = os.path.join(doc, number_id)
                with open(file_path, "w") as f:
                    f.write(f"Student No: {student_no}\n")
                    f.write(f"Full Name: {student_name[0]}, {' '.join(student_name[1:-2])} {student_name[-1]}.\n")
                    f.write(f"Program: {program}\n")
                    f.write(f"Age: {age}\n")
                    f.write(f"Gender: {gender}\n")
                    f.write(f"Birthday: {birthday}\n")
                    f.write(f"Contact No: {contact}\n")
                print("\n✅ Student record added successfully.\n")
                break

            except ValueError as e:
                print(e)

    elif choice == 2:
        print("\n===== Open Student Record =====\n")
        try:

            # Student number input and validation
            number = input("Student Number: ").strip()
            if not numbers(number) or not number:
                raise ValueError("Please enter a valid student number.\n")
            
            # Construct file path and check existence
            file_name = "student_" + number + ".txt"
            file_path = os.path.join(doc, file_name)

            # Check if file exists
            if not os.path.exists(file_path):
                print("\n❌ Student record not found.\n")
                continue
            
            # Read and display file content
            print(f"\n===== Student Record {number} =====\n")
            with open(file_path, "r") as f:
                print(f.read())
                print("===============================\n")
                
        except Exception as e:
            print(f"An error occurred: {e}\n")
            continue

    elif choice == 3:
        # Exit the program
        print("\nExiting... Goodbye!")
        break
    else:
        # Invalid choice handling
        print("\nSelect from the choices only.\n")
        continue
