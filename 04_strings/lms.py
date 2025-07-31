# Enhanced LMS Grade Tracker with String Operations
# Variables - Data types - operators - casting - conditionals
# loops - strings - slicing - indexing - string operations

print("=" * 30)
print("Enhanced LMS Grade Tracker")
print("=" * 30)

# Validate id
student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID: ")
    # check if valid id based on - sign
    if student_id.startswith("-") and student_id[1:].isdigit():
        print("Please input positive values only")
    elif student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Please input non-zero value")
    else:
        print("Enter Only Numbers")

print(student_id)      
# format id
formatted_id = "STU" + str(student_id).zfill(5)  
print(formatted_id)      

# Validate name
student_name_valid = False
while not student_name_valid:
    student_name = input("Enter Your Name: ")    
    # student_name = student_name.strip().capitalize()
    student_name = student_name.strip().title()
    # strip will remove front and back spaces, not in between
    
    # name check should have only alphabets
    name_check = student_name.replace(" ","")
    
    # look for only alphabets
    if name_check.isalpha() and len(student_name) >=3:
        student_name_valid = True
        print("Name: "+ student_name)
    else:
        if not name_check.isalpha():
            print("Name should container only letters")
        elif len(student_name) < 3:
            print("Name should have at least 3 characters")

# email generation
name_part = student_name.split()
# print(name_part)
first_name = name_part[0].lower()
# print(first_name)
student_email = first_name+"."+str(student_id) + "@university.edu" 
print(student_email)   

# Discount Calculation
base_course_fee_valid = False
while not base_course_fee_valid:
    base_course_fee = input("Enter Your Course Fee: ")
    # check if valid id based on - sign
    if base_course_fee.startswith("-") and base_course_fee[1:].isdigit():
        print("Please input positive values only")
    elif base_course_fee.isdigit():
        base_course_fee = int(base_course_fee)
        if base_course_fee > 0:
            base_course_fee_valid = True
        else:
            print("Please input non-zero value")
    else:
        print("Enter Only Numbers")

# calculation of fee
discount = 0
print("Enter Description")
description = input()

if description.lower().find("reference") != -1:
    discount+=5000

if "scholarship" in description:
    discount+=7000

if "promo" in description:
    discount+=3000
    
final_fee = base_course_fee - discount

print(f"Base Course Fee: {base_course_fee}")
print(f"You Got Discount: {discount} ")
print(f"After Discount Pay: {final_fee}")