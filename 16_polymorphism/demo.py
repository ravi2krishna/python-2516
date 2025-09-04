# Polymorphism
class Dog:
    def speak(self):
        print ("Dog Woof")

class Cat:
    def speak(self):
        print("Cat Meow")

dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# Pre defined - use cases for Polymorphism
print(len("hello"))
print(len([1,2,3]))
print(len({"a":1,"b":2}))

# Based On Operators (Operator Overloading)
print(2 + 3)
print("Hi" + " how are you")
print([1,2] + [3])

# common use case functionality
class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 5 * 5
    
def print_area(shape):
    print("Area", shape.area())

print(print_area(Circle()))    
print(print_area(Square()))   

# Real Word Use Case - Database Connection
class MySQL:
    def connect(self):
        return "Connected To MySQL"

class PostgresSQL:
    def connect(self):
        return "Connected To PostgresSQL"

def open_db_connection(db):
    print(db.connect())

open_db_connection(MySQL())
open_db_connection(PostgresSQL())

# Method Overloading - not accepted in python
class MathOps:
    def add(self,a,b):
        return a + b

    def add(self,a,b,c):
        return a + b + c

add_obj = MathOps()
print(add_obj.add(2,3)) # TypeError: MathOps.add() missing 1 required positional argument: 'c'
print(add_obj.add(2.2,3.4,2))

# Duck Typing In Python