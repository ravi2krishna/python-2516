# LMS -> Sub Feature - Student Management System
# System Information --> Tuples
SYSTEM_INFO = ("LMS Students Portal","v1.0","2025","Edify University")
ADMIN_INFO = ("admmin@edify.ai","9876543210","201")

# display system info
print("="*50)
print(f"Welcome To {SYSTEM_INFO[0]}")
print(f"Developed By {SYSTEM_INFO[3]}")
print("="*50)

# store all students --> Dictionary
students = {}

# Start with option selection
while True:
    print("Choose an option from (1-5): ")
    print("1 - Add Student")
    print("2 - Update Student")
    print("3 - Delete Student")
    print("4 - List All Students")
    print("5 - Exit System")
    
    choice = input("Enter Your Choice: ")
    
    if choice == "1":
        print("Performing Operation 1")
        student_id = input("Enter Student ID: ")
        # student exists
        if student_id in students:
            print("Student Already with this ID exists in system!")
        else:
            name = input("Enter Student Name: ").title()
            # store multiple scores
            scores = []
            while True:
                score_input = input("Enter a score or type done: ")
                # validate if input is number or done
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("Score should be between 0-100")
                else:
                   print("Score should be Number Only") 
        
            # store multiple unique skills
            skills = set()
            while True:
                skill_input = input("Enter a skill or type done: ")
                if skill_input == "done":
                    break
                skills.add(skill_input.strip().title())
            
            # save student details received so far
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("Student Added Successfully!")
            
            # For Verification print student
            print(students)
                       
    elif choice == "2":
        print("Performing Operation 2")
        student_id = input("Enter Student ID To Modify: ")
        if student_id in students:
            new_name = input("Enter New Name To Update: ").title()
            students[student_id]["name"] = new_name
            print("Student Updated Successfully!")
        else:
            print("Student ID Doesn't Exist!")
        print(students)
        
    elif choice == "3":
        print("Performing Operation 3")
        student_id = input("Enter Student ID To Delete: ")
        removed = students.pop(student_id,None)
        if removed:
            print("Student Removed Successfully!")
        else:
            print("Student ID Doesn't Exist!")
        print(students)
        
    elif choice == "4":
        print("Performing Operation 4")
        # id - student_id
        # skills 
        # scores
        # students
        if not students:
            print("No Students Available")
        else:
            print("="*50)
            print("Students Details")
            print("="*50)
            
            for sid, data in students.items():
                name = data["name"]
                scores = data["scores"]
                
                if scores:
                    avg = sum(scores)/len(scores)
                else:
                   avg = 0
                
                if scores:
                    top_score = max(scores)  
                else:
                    top_score = 0    
                
                skills = data["skills"]
                print(f"ID: {sid}")
                print(f"Name: {name}")
                print(f"Scores: {scores}")
                print(f"Average Score: {avg}")
                print(f"Top Score: {top_score}")
                print(f"Skills: {skills}")
                print(f"Skills Count: {len(skills)}")

    elif choice == "5":
        print("Performing Operation 5")
        print("="*50)
        print("Contact Admin For Further Queries")
        print(f"Admin Contact: {ADMIN_INFO[1]}")
        print(f"Admin Email: {ADMIN_INFO[0]}")
        print("="*50)
        break
    else:
       print("Invalid Choice Only (1-5) available") 