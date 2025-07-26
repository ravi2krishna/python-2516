student_name=input("enter student name: ")
student_grade=int(input("enter student grade between 1-12: "))
base_tutionfee=int(input("enter base tution fee: "))
topper=input("enter wheather the student is acadamic topper or not (yes/no): ")

if not (1 <= student_grade <= 12):

    print("grade not valid enter between 1 to 12")
else:
    discount=0
    if 9<= student_grade <=12  :
       if topper.lower()== "yes":
        discount = 20
       else :
        discount = 10
    elif 6<= student_grade <=8:
        discount = 5
    elif student_grade <6:
        discount = 0
#for additionl discounts
    match student_grade:
     case 10:
        discount += 3
     case 12:
        discount += 5  
        

total_fee=  base_tutionfee -(discount/100) *base_tutionfee
total_discount=discount
discount_amountsaved=base_tutionfee-total_fee

print(f"student name is {student_name}")
print(f"grade level is {student_grade}")
print(f"academic topper  {topper}")
print(f"base tution fee {base_tutionfee}")
print(f"total discount percentage {total_discount}")
print(f"discount amount saved {discount_amountsaved}")
print(f"final tution fee after discount is {total_fee}")
    