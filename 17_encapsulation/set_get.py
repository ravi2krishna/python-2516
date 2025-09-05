# Without Setters & Getters 
class Student:
    def __init__(self,age):
        self.__age = age # directly assigning values without any validations

s = Student(20) 
print(s._Student__age)  # Direct Access

s._Student__age = -5 # No validations 
print(s._Student__age)

# With Setters & Getters 
class Student:
    def __init__(self,age):
        self.__age = age 
    
    # setter
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age")
        
    # getter
    def get_age(self):
        return self.__age 
s = Student(15)
s.set_age(-5)
print(s.get_age())