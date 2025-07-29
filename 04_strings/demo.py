# Using '' or "" or """ is valid for single line strings
data_1 = "hello"
data_2 = 'hello'
data_3 = '''hello'''
data_4 = """hello"""

print(data_1)
print(data_2)
print(data_3)
print(data_4)

# multi line strings -> """ are must
# Below is not valid
# python_desc = "Python is a high-level, general-purpose 
# programming language. Its design philosophy emphasizes 
# code readability with the use of significant indentation"

python_desc = """Python is a high-level, general-purpose 
programming language. Its design philosophy emphasizes 
code readability with the use of significant indentation"""

question = "How are you ?"
# using a single quote inside single quotes is not valid
# if you want to include single quote, use double quotes
# answer = 'i'm fine' 
answer = "i'm fine"
print(answer)

# answer = "im "good""
answer = 'im "good"'
print(answer)

# if you need both use ''' or """
answer = """ i'm fine and "good" """
print(answer)

# Accessing
text = "python"

# Python uses indexing for accessing individual characters 
print(text[0])
print(text[2])

print(text[-2])

# Invalid range
# print(text[10]) # IndexError: string index out of range

text = "python"
# using for loop to access each character
for i in text:
    print(i)

text = "python"
print(text[1])
print(text[2])
print(text[3])

text = "python is very easy to learn"

# Slicing
text = "python"
print(text[0:3]) # last is excluded -> pyt
print(text[1:4]) # last is excluded -> yth
print(text[1:]) # last is excluded -> ython
print(text[:4]) # last is excluded -> pyth
print(text[:]) # last is excluded -> python

# if step is not defined, default step is 1
print(text[1:4:1]) # last is excluded -> yth
text = "pythonisveryeasytolearn"
text1 = "python is very easy to learn"
print(text[0:16:2]) # last is excluded -> pt
print(text1[0:16:2]) # last is excluded -> pt

# For negative indexing default step is 1
# text = "python" # ValueError: slice step cannot be zero
# print(text[1:4:0]) 
text = "python"
print(text[-4:-1]) # tho
print(text[-4:-1:1]) # tho
print(text[-4:-1:-1]) # 

print(text[-4:-1:-1]) # 
        #     0  1  2  3  4  5 (positive)
        #     p  y  t  h  o  n 
        #    -6 -5 -4 -3 -2 -1 (negative)
# start -4 -> index -> 2 -> t
# end -1 -> index -> 5 -> n (excluded)
# step -1 -> move backwards

# IMP: You starting at index 2 and trying to go backward to
    # index 5 -> nothing
    
text = "python"
print(text[1:4:-1])
        #     0  1  2  3  4  5 (positive)
        #     p  y  t  h  o  n 
        #    -6 -5 -4 -3 -2 -1 (negative)
# start 1 -> index -> 1 -> y
# end 4 -> index -> 4 -> o (excluded)
# step -1 -> move backwards

# Typical use case of backward step
text = "python"
print(text[::-1])

# ohty
print(text[-2:-5:1])
print(text[-2]+text[-3]+text[-5])


# String Immutability
# TypeError: 'str' object does not support item assignment
text = "python"
# text[0] = "P"
print(text)

# Reassigning is okay 
text = "python"
text = "Python" # new 
print(text)

new_text = "J" + text[1:]
print(new_text)

# Concat(+) Join Strings 
# Repeat (*) Repeat Strings
# Concat -> join multiple strings
str = "hi"
print(str * 5)

# String Operations -> String Methods
print(dir(str))

mobile_number = input("Enter Mobile Number: ")
valid_number = mobile_number.isdigit()
print(valid_number)

pan_number = input("Enter PAN Card Number: ")
valid_pan_number = pan_number.isalnum()
fomart_valid_pan_number = pan_number.upper()
print(fomart_valid_pan_number)

