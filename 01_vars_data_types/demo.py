# for comments
# print(hello)
# print(9)
# print("a")
# a=10
# b=20
# print(a+b)

# import keyword
# print(keyword.kwlist)

# from math import sqrt
# print(sqrt(16))

# Store Data --> Type Of Data
student_name_1 = "Ravi"
print(type(student_name_1))
print(id(student_name_1))

student_name_2 = "Krishna"
print(id(student_name_2))

student_1_age = 20
print(type(student_1_age))
print(id(student_1_age))

student_2_age = 20
print(id(student_2_age))

student_gpa = 8.5
print(type(student_gpa))
print(id(student_gpa))

# int, flot are immutable data

# define some complex data 
# List is mutable data type
list_1 = [1,2,3]
list_2 = [1,2,3]
print(id(list_1))
print(id(list_2))

x = "python"
y = " is "
z = " awesome"

print(x+y+z) 
# python is awesome --> String Concatenation (+) 

x = 10
y = 20
print(x+y) # --> Addition Operator
z = " awesome"
# print(x+z) --> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 10 awesome
print(x,z)

x,y,z = "one","two","three"
print(x,y,z)

# x,y,z = "one","two","three","four" --> ValueError: too many values to unpack (expected 3)
print(x,y,z)

x = y = z = "One"
print(x)
print(y)
print(z)