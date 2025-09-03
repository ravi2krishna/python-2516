# Functionality for multiple user types
class Person:
    def __init__(self,person_id,person_name,person_age):
        self.person_id = person_id
        self.person_name = person_name
        self.person_age = person_age
    
    def display_info(self):
        print("====== Info ======")
        print(f"ID: {self.person_id}")
        print(f"Name: {self.person_name}")
        print(f"Age: {self.person_age}")

# Student --> type of person
class Student(Person):
    def __init__(self,student_id,student_name,student_age):
        super().__init__(student_id,student_name,student_age)

# Trainer --> type of person, but has his own data also additionally
class Trainer(Person):
    def __init__(self,trainer_id,trainer_name,trainer_age,trainer_desc):
       super().__init__(trainer_id,trainer_name,trainer_age) 
       self.trainer_desc = trainer_desc
    
    def display_info(self): 
        super().display_info()
        print(f"Description: {self.trainer_desc}")
    
# student
s1 = Student(101,"John",20)
s1.display_info()

# Trainer
t1 = Trainer(102,"Doe",40,"Python Instructor")
t1.display_info()