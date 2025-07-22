# variables
student_id = 101
student_name = "Ravi"
student_age = 20
quiz_score = 75
assignment_score= 85
exam_score = 80
student_attendance = 65

# total score
total_score = quiz_score + assignment_score + exam_score

# average score
average_score = total_score / 3 # static
# average_score = total_score / len(total_score) # dynamic 

# Student Passed
student_passed = average_score >= 75

# Attendance simulation
student_attendance += 1

# award eligibility
award_eligibility = student_attendance >= 90 and student_passed

print(f"Student Name: {student_name}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")
print(f"Student Passed: {student_passed}")
print(f"Student Current Attendance: {student_attendance}")
print(f"Student Awarded: {award_eligibility}")
