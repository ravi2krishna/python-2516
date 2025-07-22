# Arithmetic Operators
num1 = 3
num2 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2) # 1.5
print(num1%num2)
print(num1//num2) # floor division
print(num1**num2) # exponentiation (3 ^ 2)

# Compound Assignment Operators
num = 10
# num = num + 5
num+=5
print(num)
num*=5
print(num)

# Comparison / Relational Operators
num1 = 3
num2 = 2

print(num1>num2)
print(num1<num2)
print(num1!=num2)

# Logical Operators
a = 10
b = 5
c = 3
d = 8

result_and = a > b and b < c # T and F -> F
print(result_and)
result_or = a > b or b < c # T or F -> T
print(result_or)
result_not = a > b # -> T
print(not result_not) # T -> F

# Membership Operators
text = "python is eazy"
is_z_present = "z" in text
print(is_z_present)

list_nums = [1,2,3,4,5]
is_5_present = 5 in list_nums
print(is_5_present)

is_z_not_present = "z" not in text
print(is_z_not_present)

# Identity Operators
num1 = 10
num2 = 10
print(id(num1))
print(id(num2))
print(num1 is num2)

num1_list = [10,20]
num2_list = [10,20]
print(id(num1_list))
print(id(num2_list))
print(num1_list is num2_list)

print(num1_list is not num2_list)

#Bitwise Operators
a = 5 # 0000000000000101
b = 3 # 0000000000000011
resultand = a & b # 0000000000000001
print(resultand)

resultor = a | b # 0000000000000111
print(resultor) 

resultxor = a ^ b # 0000000000000110
print(resultxor) 

resultnot = ~b
print(resultnot) # 0000000000000011 -> 1111111111111100

b = 3 # 0000000000000011
print(3<<2) # 0000000000001100 --> 12
print(3<<1) # 0000000000000110 --> 6
print(3<<3) # 0000000000011000 --> 24

b = 3 # 0000000000000011
print(3>>2) # 0000000000000000 --> 0
print(3>>1) # 0000000000000001 --> 1
print(8>>2) # 0000000000001000 --> 0000000000000010

# c = -4 # 1111111111111111
print(-4>>3) # 1111111111111111