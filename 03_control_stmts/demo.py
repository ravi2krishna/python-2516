# if condition
value = -10

# check if given value is positive 
if value>0:
# print(f"Given {value} is Positive")  # IndentationError: expected an indented block  
    print(f"Given {value} is Positive")
#  print("Code Will Not Execute")  # IndentationError: unindent does not match any outer indentation level  
    print("Code Will Execute")

# condition for checking a number is in range or not (10 to 20)    
num = 12
if num >=10 and num <=20:
 print(f"Given num {num} is in range")   

# check if given value is positive or negative
value = 10
if value>0:
    print(f"Given {value} is Positive")
else:
    print(f"Given {value} is Negative")

# input() --> for taking inputs
# print("Enter Your Email: ")       
email = input("Enter Your Email: ")  
print(f"Welcome: {email}")     

# Check Vote Eligibility Using If-else
age = int(input("Enter Your Age: ") )
if age>=18:
    print(f"You Can Vote")
else:
    print(f"You Cannot Vote") 
# TypeError: '>=' not supported between instances of 'str' and 'int'

# Check Vote Eligibility Using Ternary Operator
# value_if_true if condition else value_if_false 
age = int(input("Enter Your Age: ") )
status = "You Can Vote" if age>=18 else "You Cannot Vote"
print(status)

# elif ladder
avg_score = int(input("Enter Your Average Score: ") )
if avg_score >= 90:
    print("A Grade")
elif avg_score >= 75:
    print("B Grade")
elif avg_score >= 60:
    print("C Grade")
elif avg_score >= 50:
    print("D Grade")
elif avg_score >= 35:
    print("E Grade")    
else:
    print("FAIL")

# Match Case
# SyntaxError: invalid syntax -> Older version python2/3 --> 3.1 supports
choice = int(input("Enter Your Choice: "))
match choice:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case _:
        print("Invalid")

# Nested Conditions Scenario
# Club Entry --> if age is 21 or above and also a valid ID Should be present
age = 22
has_id = False

if age >= 21:
    if has_id:
        print("You are allowed to enter")
    else:
       print("You Need an ID to enter") 
else:
    print("You Are Too Young to enter") 
