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

# Working with csv files
# read data
import csv
with open("sample_data.csv","r") as file_data:
    csv_reader = csv.reader(file_data)
    print(csv_reader)
    for row in csv_reader:
        # print(row)        
# get the customers from hyderabad --> first priority ship products to hyd customers
        # print("Hyderabad Customers")
        # if row[3] == "hyderabad":
        #     print(row)
# get the customers for gmail  --> first priority ship products to hyd customers
        if row[1].endswith("@gmail.com"):
            print(row) 

# DictReader --> gives the dictionary object
with open("sample_data.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    print(csv_reader)
    for row in csv_reader:
        if row["email"].endswith("@gmail.com"):
            print(row)
            
            
# Now writing the data
with open("write_data.csv","w") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerow(['name','email','mobile','location'])
    csv_writer.writerow(['ravi','ravi@gmail.com','9909090','hyd'])
    csv_writer.writerows([['ravi','ravi@gmail.com','9909090','hyd'],['john','johnjohn@gmail.com','9909090','hyd']])
      
# Now appending the data              
with open("write_data.csv","a") as file_data:
    csv_writer = csv.writer(file_data)
    csv_writer.writerows([['user1','user1@gmail.com','9909090','hyd'],['user2','user2@gmail.com','9909090','hyd']])
    

# Working with JSON Data
import json
student = {
   "id": 101,
   "name": "Ravi",
   "course": "Python Full Stack",
   "skills": ["Python", "Git", "AWS"],
   "score": 89.5
}

print(type(student))
# Now writing the data
with open("student.json","w") as file_data:
    json.dump(student, file_data, indent=4)

# Now read the data
with open("student.json","r") as file_data:
    json_data = json.load(file_data)
    print(json_data)
    print(type(json_data))
    print(json_data['name'])
    print(json_data['skills'][0])
    
# Ops b/w Jon & Py Data
# convert python json data to string data 
student_json = json.dumps(student)
print(student_json)

# convert string data to json
json_string = '{"id": 102, "name": "Anjali", "course": "Data Science"}'
print(type(json_string))
stu_data = json.loads(json_string)
print(stu_data)
print(type(stu_data))