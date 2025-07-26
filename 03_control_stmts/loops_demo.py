# Implementation Of Loops

# while loop
# while condition:
#     statements
count = 1
while count <=5 :
    print(count)
    count+=1
    
# while True:
#     print("Infinite Loop")    

# Best use case to understand while
password = "123"    
user_input = ""

while user_input != password:
    user_input = input("Enter Password ")
print("Access Granted")    
    
# for loop
# for element in sequence:
#     statements    
text = "python"
print(dir(text))
for i in text:
    print(i)

# We cannot use for to iterate non iterable objects
just_num = 10
print(dir(just_num))
# for i in num:
#     print(i)    
    

# We can use for to iterate iterable objects
list_num = [10] # List --> iterable objects
print(dir(list_num))
for i in list_num:
    print(i)     
    
# Manual Work
print("Hi") 

# Say 10 Time Hi - Manually
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 
print("Hi") 

print("==========") 

# Say 10 Time Hi - Automated
for i in range(10):
    print("Hi")

for i in range(1,10,2):
    print(i)   
    
    
# let's print even nums between 1 - 20 -> while
# 1st approach
i = 2
while i <=20:
    print(i)
    i+=2
print("==========") 
# 2nd approach
i = 2
while i <=20:
    if i % 2 == 0:
        print(i)
    i+=1

print("==========")
# let's print even nums between 1 - 20 -> for
# 1st approach
i = 2
for i in range(2,21,2):
    print(i)

# Nested For loop
# Maths Table
for i in range(1,4):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")      
print("==========")
# Nested while loop
# Maths Table
i = 1
while i < 4:
    j = 1
    while j < 3:
        print(f"{i} X {j} = {i*j}")
        j += 1
    i += 1      
    
# break demo
for i in range(5):
    if i == 3:
        break # terminate loop when i is 3
    print(i)
    
# continue demo    
for i in range(5):
    if i == 3:
        continue # skip 4th iteration when i is 3 (based on index)
    print(i)

# pass demo
if (5>9):
     pass   