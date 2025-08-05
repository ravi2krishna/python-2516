# define a list 
empty_list = []
print(type(empty_list))
print(empty_list)

# define a list with nums
list_nums = [10,20,30,40,50]
print(type(list_nums))
print(list_nums)

# define a list with texts
list_courses = ["python","java","cloud","devops","html"]
print(type(list_courses))
print(list_courses)

# define a list with mixed data
list_mixed = [10,20,30,40,50,"python","java","cloud","devops","html",3.15]
print(type(list_mixed))
print(list_mixed)

# list inside list
list_nest = [10,20,30,40,50,["python","java","cloud"]]
print(type(list_nest))
print(list_nest)

# using class list
empty_list = list()
print(type(empty_list))
print(empty_list)

# define a list with nums
list_nums = list([10,20,30,40,50])
print(type(list_nums))
print(list_nums)

# define a list with nums
num = 10
print(type(num))
# list_nums = list(10) # TypeError: 'int' object is not iterable
list_nums = list([10])
print(type(list_nums))
print(list_nums)

# Accessing the data in list
list_nums = [10,20,30,40,50]
first_list_nums = list_nums[0]
last_list_nums = list_nums[-1]

# Indexing
print(first_list_nums)
print(last_list_nums)

# Slicing
list_nums = [10,20,30,40,50]
print(list_nums[:])
print(list_nums[1:4:1])
print(list_nums[1:4:-1])
print(list_nums[::-1])

# get to know memory management with data
num1 = 10
num2 = 10

print(id(num1))
print(id(num2))

list_1 = [10,20,30,40,50]
list_2 = [10,20,30,40,50]

print(id(list_1))
print(id(list_2))

print(id(list_1[0]))
print(id(list_2[0]))
print(id(num1))
print(id(num2))

list_nums = [10,20,30,40,50]
# print[list_nums[10]] # IndexError: list index out of range
# print(dir(list_nums))

# Looping can be done as it's an iterable
list_nums = [10,20,30,40,50]
for i in list_nums:
    print(i)
    
# using range 
custom_list = list(range(0,26,5))
print(custom_list)   

# perform any operations with operators
custom_list = list(range(0,26,5))
for i in custom_list:
    print(i*2)   

# perform some conditionals
days = ["sun","mon","tue","wed","thu","fri","sat"]
day = input("Enter day name in a week: ")
if day in days:
    print("Day Exists")        
else:
    print("Invalid Day In Week")        

# Duplicates are allowed
list_nums = [10,20,30,40,50,50,50,30]    
print(list_nums)

# List Operations
list_nums = [10,20,30,40,50]
# print(dir(list_nums))

# 1 append() -> adds a single element, at end of list
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.append(60)
print(list_nums)

# list_nums.append(70,80) # list.append() takes exactly one argument
list_nums.append([70,80])
print(list_nums)

list_nums.append("hello")
print(list_nums)

list_nums.append("hello")
print(list_nums)

#  2 extend() - can add only iterables, so elements
# are added as individuals, not as nested
list_nums = [10,20,30,40,50]
print(list_nums)
# list_nums.extend(60) # TypeError: 'int' object is not iterable
list_nums.extend([60])
print(list_nums)

list_nums.extend([70,80])
# list_nums.extend([70,80],[90,100])
print(list_nums)

# NOTE both append and extend takes only one argument
list_nums.extend("hello")
print(list_nums)

# 3 insert() -> based on index insert an element
list_nums = [10,30,40,50]
print(list_nums)
list_nums.insert(1,20)
print(list_nums)

list_nums.insert(len(list_nums),60)
print(list_nums)

list_nums.insert(10,100)
print(list_nums)
# print(list_nums.index(100))

# 4 pop() -> removes an element, by default removes last index element 
list_nums = [10,20,30,40,50]
print(list_nums)
removed_element = list_nums.pop()
print(removed_element)
print(list_nums)

list_nums = [10,20,30,40,50]
print(list_nums)
removed_element = list_nums.pop(1)
print(removed_element)
print(list_nums)

# 5 remove() -> removes the matching value, not based on index
list_nums = [10,20,30,40,50,10]
print(list_nums)
list_nums.remove(10)
print(list_nums)

# 6 clear() -> removes all the elements
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.clear()
print(list_nums)

# 7 index() -> returns the index position of element, 
list_nums = [10,20,30,40,50]
print(list_nums.index(40))
# print(list_nums.index(60))

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums.index(20,2)) # start
print(list_nums.index(20,4,8)) # start

# 8 count() -> counts and returns number of times a element present
list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums.count(10))

# 9 reverse() -> reverses the elements of list, and updates original list
list_nums = [10,20,30,40,50]
print(list_nums)
list_nums.reverse()
print(list_nums)

# slicing reverses the elements of list, and don't update original list
list_nums = [10,20,30,40,50]
print(list_nums)
print(list_nums[::-1])
print(list_nums)

# 10 sort() -> sorts the list, default is ascending
list_nums = [10,30,20,40,50]
print(list_nums)
print(list_nums.sort()) # ascending
print(list_nums)

list_nums = [10,30,20,40,50]
print(list_nums)
print(list_nums.sort(reverse=True)) # descending
print(list_nums)

names = ["zohan","ramu","anju"]
names.sort()
print(names)

mixed_data = ["zohan","ramu","anju",10,20]
# mixed_data.sort() # mixed data cannot be sorted
print(mixed_data)

# 11 copy() -> creates a shallow copy, meaning when we modify the shallow copy
# original copy will not affect 
list_nums = [10,20,30,40,50]
print(list_nums)

bk_list_nums = list_nums.copy()
print(bk_list_nums)

bk_list_nums.append(60)
print("Backup: ",bk_list_nums)
print("Original: ",list_nums)

# soft copy - use assignment operator
list_nums = [10,20,30,40,50]
print(list_nums)

bk_list_nums = list_nums # soft copying
bk_list_nums.append(60)
print("Backup: ",bk_list_nums)
print("Original: ",list_nums)