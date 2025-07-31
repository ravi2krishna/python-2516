# LMS Grade Tracker in Python

# Prompt Student For Input Details
student_id = int(input("Enter Your ID: "))  # Read integer input
student_name = input("Enter Your Name: ")  # Read string input

# Attendance updated by admin/trainer
attendance = 50.0
number_of_subjects = 0  # Number of subjects
total_score = 0  # Initialize total score

# Design User Input
continue_input = "yes"

while continue_input == 'yes' or continue_input == 'Yes':
   # current_score a local variable to keep track of current score
   current_score = int(input(f"\nEnter score for Subject {number_of_subjects + 1}: "))
   continue_input = input("Do you want to enter another score? (yes/no): ")
   # increment number of subjects
   number_of_subjects += 1
   # Update total score
   total_score += current_score

# Calculate average score
average_score = total_score / number_of_subjects

# Determine performance level
if average_score >= 85:
   performance = "Excellent"
elif average_score >= 70:
   performance = "Good"
elif average_score >= 50:
   performance = "Average"
else:
   performance = "Needs Improvement"

# Check Attendance Status
attendance_status = "WARNING - Low Attendance" if attendance < 75 else "OK - Attendance Satisfied"

# Display the results using f-strings
print("\n========== Student Details ==========")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Student Attendance: {attendance}%")
print(f"Total Score: {total_score}")
print(f"Total Number Of Subjects: {number_of_subjects}")
print(f"Average Score: {average_score}")
print(f"Performance: {performance}")
print(f"Attendance: {attendance_status}")
print("=====================================")