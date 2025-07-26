# Assume the correct OTP is already stored in a variable.
# Ask the user to input a 4-digit OTP.
# If the OTP entered is not 4 digits, display
# OTP Must be 4 digit number only
# If the OTP is correct, display:
# Correct OTP - Success
# If the OTP is incorrect, decrease the attempts count.
# After 3 incorrect attempts, display
# Maximum attempts done, try after 24 Hours

# OTP / Verification Code Simulation
import random

otp = random.randint(1000,9999)
print(otp)

# Logic
attempts = 3

while attempts:
    user_otp = int(input("Enter OTP: "))
    if len(str(user_otp))!=4:
        print("OTP Must be 4 digit number only")
    if user_otp == otp:
        print("Correct OTP - Success")
        break
    attempts-=1
else:
    print("Maximum attempts done, try after 24 Hours")    
