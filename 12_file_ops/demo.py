# I have a file on persistent storage

# we have open function 

# 1st syntax
# open ("filepath",mode) 
    # mode - r w a
file = open("file.txt","r")
# print(type(file))
print(file)
print(file.closed)
file.close()
print(file.closed)

# 2nd syntax -- recommended
# with open ("filepath",mode) 
    # mode - rwa
# read mode    
with open("file.txt","r") as file_new:
    # print(type(file_new))
    print(file_new)
    # print(file_new.read()) # closes the connection
    
    # for character in file_new.read(): # character by character
    #     print(character) 
    
    # read line by line
    # print(file_new.readline())
    # print(file_new.readline())
    
    # print(file_new.readlines()) # read all lines
    for line in file_new.readlines():
        print(line.strip())
    
# print(file_new.closed)

# create file -> using write (w) mode
# default behavior is overwrite
# write mode
with open("new.txt","w") as file_new:
    # print(file_new)
    file_new.write("Welcome To Java \n")
    file_new.write("Welcome To Python \n")
    file_new.write("Welcome To Git")

with open("data.txt","w") as file_new:
    # print(file_new)
    file_new.writelines(["Welcome To Java \n", "Welcome To Python \n", 
"Welcome To Git"])
    
    
# append mode -> add to exiting data without overwrite
with open("data.txt","a") as file_new:
    # print(file_new)
    file_new.writelines(["Welcome To Cloud \n", "Welcome To DevOps \n", 
"Welcome To DS"])
    
# delete a file
# os module 
import os
os.remove("data.txt")