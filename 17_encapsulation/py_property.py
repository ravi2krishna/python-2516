# @property decorator --> python way of setters & getters
class Student:
    def __init__(self,age):
        self.__age = age
    
    @property
    def age(self): # getter
        return self.__age
    
    @age.setter
    def age(self,age): # setter
        if age > 0:
            self.__age = age
        else:
            print("Invalid Age")
        
s = Student(20)
print(s.age)

s.age = 25
print(s.age)

s.age = -5
print(s.age)