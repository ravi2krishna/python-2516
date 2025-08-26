# Exception Handling

# When there are no errors, nothing to handle
print("Program Execution Started")
num1 = 10
num2 = 5
print(num1/num2)
print("Program Execution Completed")
print("="*50)

# When there are errors, see how python handles them --> abruptly stops the execution
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero # Division by zero is undefined in mathematics
#   File "/Users/ravi/Documents/python-2516/13_execeptions/demo.py", line 15, in <module>
#     print(num1/num2)
# ZeroDivisionError: division by zero
print("Program Execution Completed")
print("="*50)


# When there are errors, see how you can handle the errors - single error
print("Program Execution Started")
num1 = 10
num2 = 5
# ZeroDivisionError: division by zero # Division by zero is undefined in mathematics
try:
    print(num1/num2) 
except:
    print("OOPS! You cannot divide by zero in maths it's undefined")
print("Program Execution Completed")
print("="*50)

# When there are errors, see how you can handle the errors - multiple errors
import sys
print("Program Execution Started")
data = [1,2,'python',0,5]
data = [1,2,3,4,5]
for i in data:
    try:
        print(1/i)
        # TypeError: unsupported operand type(s) for /: 'int' and 'str' --> 'python'
        # ZeroDivisionError: division by zero --> 0
    except TypeError:
        # print(sys.exc_info())
        print("OOPS! Don't pass strings, we cannot divide strings and numbers")
    except ZeroDivisionError:
        print("OOPS! You cannot divide by zero in maths it's undefined")
        
print("Program Execution Completed")    
print("="*50)

# When there are errors, see how you can handle the errors - single error
print("Program Execution Started")
num1 = 10
num2 = 5
# ZeroDivisionError: division by zero # Division by zero is undefined in mathematics
try:
    print(num1/num2) # login info is correct 
except:
    print("OOPS! You cannot divide by zero in maths it's undefined")
else:
    print("Calculation Successful") # OTP Verify --> Only when login info is correct
finally:
    print("Program Execution Completed")
print("="*50)

# Exception class
# print(help(Exception))

# Based On my Req --> we need a custom exception


class InvalidScoreError(Exception):
    pass

try:
    score = int(input("Enter Score (0-100): "))
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between (0-100)")
    print("Your Score is valid")
except InvalidScoreError as e:
    print("Error: ", e)
    
class AgeTooYoungError(Exception):
    pass

class NoIDError(Exception):
    pass

try:
    age = int(input("Enter Your Age: "))
    if age < 18:
        raise AgeTooYoungError
    has_id = input("Do You have id ? (yes/no)")
    if has_id != "yes":
        raise NoIDError
except AgeTooYoungError: 
    print("You must be at least 18 Years Old To Register")   

except NoIDError:
    print("You must have an ID To Register")   
else:
    print("Registration Successful")