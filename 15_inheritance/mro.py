# Method Resolution Order
class A:
    def show(self):
        print("A Show")

class B():
    def show(self):
        print("B Show")

class C(B,A):
    pass

obj = C()
obj.show()
print(C.mro())

# super()
class Parent:
    def greet(self):
        print("Hello From Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("hello from child")

child = Child()
child.greet()