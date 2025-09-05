# Private 
class A:
    def __init__(self,a,b):
        self.__a = a # private 
        self.__b = b # private 

obj = A(10,20)

# Accessing Private
print(obj._A__a) # Name Mangling 
print(obj.b)