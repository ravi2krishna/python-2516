# With Inheritance
class Student:
    
    # video functionality watching
    def watch_videos(self):
        print("="*50)
        print("Functionality For Watching Videos")
        print("W")
        print("a")
        print("t")
        print("c")
        print("h")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50)

class VideoAdmin(Student): 
# class VideoAdmin(): --> No inheritance   
    # video functionality adding
    def add_videos(self):
        print("="*50)
        print("Functionality For Adding Videos")
        print("A")
        print("d")
        print("d")
        print("i")
        print("n")
        print("g")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50) 

class SuperAdmin(VideoAdmin):
# class SuperAdmin(): --> No inheritance   
    # video functionality deleting
    def delete_videos(self):
        print("="*50)
        print("Functionality For Deleting Videos")
        print("D")
        print("e")
        print("l")
        print("e")
        print("t")
        print("e")
        print("v")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print(".")
        print("="*50) 

# Test functionalities
print("Student User")    
student_user = Student()
student_user.watch_videos()

print("Video Admin User")    
va_user = VideoAdmin()
va_user.watch_videos() # inherited from Student
va_user.add_videos()

print("Super Admin User")   
sa_user = SuperAdmin()
sa_user.watch_videos() # inherited from Student
sa_user.add_videos()   # inherited from VideoAdmin
sa_user.delete_videos()