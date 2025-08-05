# Tuples
empty_tuple = ()
print(type(empty_tuple))
print(empty_tuple)

# Numbers
tuple_nums = (10,20,30,40,50)
print(tuple_nums)

# Texts
tuple_courses = ("python","java","cloud")
print(tuple_courses)

# Mixed 
tuple_mixed = ("python","java","cloud",10,20,30,40,50,5.5)
print(tuple_mixed)

# Empty Tuple
empty_tuple = tuple()
print(type(empty_tuple))
print(empty_tuple)

# Numbers
tuple_nums = tuple((10,20,30,40,50))
print(tuple_nums)

# Texts
tuple_courses = tuple(("python","java","cloud"))
print(tuple_courses)

# Mixed 
tuple_mixed = tuple(("python","java","cloud",10,20,30,40,50,5.5))
print(tuple_mixed)

# tuple_int = tuple(10) invalid
# tuple_int = tuple((10)) invalid
tuple_int = tuple((10,))
print(tuple_int)

# list
list_nums = [10,20,30,40,50]
print(list_nums)

tuple_nums = tuple(list_nums)
print(tuple_nums)

list_nums = list(tuple_nums)
print(list_nums)

# Accessing the data in list
tuple_nums = (10,20,30,40,50)
first_tuple_nums = tuple_nums[0]
last_tuple_nums = tuple_nums[-1]

# Indexing
print(first_tuple_nums)
print(last_tuple_nums)

# Slicing
tuple_nums = (10,20,30,40,50)
print(tuple_nums[:])
print(tuple_nums[1:4:1])
print(tuple_nums[1:4:-1])
print(tuple_nums[::-1])

# print(tuple_nums[10]) IndexError: tuple index out of range

# Looping can be done as it's an iterable
tuple_nums = [10,20,30,40,50]
for i in tuple_nums:
    print(i)
    
# using range 
tuple_nums = tuple(range(0,26,5))
print(tuple_nums)   

# perform any operations with operators
tuple_nums = tuple(range(0,26,5))
for i in tuple_nums:
    print(i*2)   

# perform some conditionals
days = ("sun","mon","tue","wed","thu","fri","sat")
day = input("Enter day name in a week: ")
if day in days:
    print("Day Exists")        
else:
    print("Invalid Day In Week")        

# Duplicates are allowed
tuple_nums = [10,20,30,40,50,50,50,30]    
print(tuple_nums)

# Tuples Operations
tuple_nums = (10,20,30,40,50)
print(dir(tuple_nums))

# index() -> returns the index position of element, 
tuple_nums = (10,20,30,40,50)
print(tuple_nums.index(30))

# count() -> counts and returns number of times a element present
tuple_nums = (10,20,30,40,50,10)
print(tuple_nums.count(10))

# Tuples Packing nd Unpacking
person = ("John",25,"Python") # Packing
# person = ("John",25,"Python",25000) ValueError: too many values to unpack (expected 3)
name,age,course = person # Unpacking

print(name)
print(age)
print(course)

t1 = ([10,20],[30,40],[50,60])
print(t1)
t1[0][0] = 100 # Valid -> Change List
print(t1)

t1 = ([10,20],[30,40],[50,60])
print(t1)
# t1[1] = [300,400] # Invalid -> change tuple
# TypeError: 'tuple' object does not support item assignment
print(t1)

l1 = [(10,20),(30,40),(50,60)]
print(l1)
# l1[0][0] = 100 #  Invalid 
# TypeError: 'tuple' object does not support item assignment
print(l1)

print(l1)
l1[1] = (300,400)
print(l1)