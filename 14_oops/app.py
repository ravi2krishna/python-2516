#     -> Instance Variables
#     -> Class Variables
#     -> Instance Methods
#     -> Class Methods
#     -> Static Variables (X) --> Class Variables
#     -> Static Method
#     -> Local Variables
class Student:
    
    # class variables -> common for all objects
    institute_name = "Digital Edify"
    
    # instance variables (__init__ : constructor)
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email 
    
    # instance method
    def info(self):
        # class level variables we use class name to access
        print("Welcome To: ",Student.institute_name) 
        
        # instance level variables we use self
        print("Student Name",self.student_name)
        print("Student Email",self.student_email)
        
        # local variable
        local_var = 20
        print(local_var)

    # class method
    @classmethod
    def change_institute(cls,new_name):
        cls.institute_name = new_name
        
    # static method --> helper functions
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
            
            
student_one = Student("one","one@gmail.com")    
student_two = Student("two","two@gmail.com")

Student.change_institute("Digital Lync")

print(Student.validate_email("one@gmail.com")) # we can access static methods with Classname
print(Student.validate_email("twogmail.com")) # we can access static methods with Classname

student_one.info() 
student_two.info() 

