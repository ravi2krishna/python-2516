class Student:
    # characteristics / data / variables / attributes 
    # student_name = "John"
    # student_email = "john@gmail.com"
    
    # special method __init__ (constructor)
    def __init__(self, student_name, student_email):
        self.student_name = student_name # self.student_name -> instance variable
        self.student_email = student_email # self.student_email -> instance variable
    
    # my custom methods -> instance method
    def info(self):
        print("Student Name: ", self.student_name)
        print("Student Email: ", self.student_email)
        
student_one = Student("one","one@gmail.com")
student_second = Student("two","two@gmail.com")
student_third = Student("three","three@gmail.com")

student_one.info()
student_second.info()
student_third.info()


        
    # method
    # def info(self):
    #     # print(Student.student_name,Student.student_email) # -> valid
    #     print(self.student_name,self.student_email)   # -> valid
    
# student_one = Student()
# student_one.info()

# student_second = Student()
# student_second.info()

# student_third = Student()
# student_third.info()
