# Encapsulation

# Public 
class A:
    def __init__(self,a,b):
        self.a = a # public 
        self.b = b # public 

obj = A(10,20)

# Accessing Public
print(obj.a)
print(obj.b)

# Protected 
class A:
    def __init__(self,a,b):
        self._a = a # Protected 
        self._b = b # Protected 

obj = A(10,20)

# Accessing Protected
print(obj.a)
print(obj.b)

# Private 
class A:
    def __init__(self,a,b):
        self.__a = a # private 
        self.__b = b # private 

obj = A(10,20)

# Accessing Private
print(obj.a)
print(obj.b)

