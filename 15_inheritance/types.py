# Types Of Inheritances

# Single Inheritance : Inherit from single parent
class Father:
    def house(self):
        print("Has House")

class Son(Father):
    def car(self):
        print("Has Car")
        
son_obj = Son()
son_obj.house()
son_obj.car()
    
# Multi Level Inheritance : A class inherits from another class, which inturn inherits 
    # from another and this can go on
class GrandParent:
    def land(self):
        print("Has Agriculture Land")    

class Father(GrandParent):
    def house(self):
        print("Has House")

class Son(Father):
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.land()
son_obj.house()
son_obj.car()

# Multiple Inheritance : One class inherits from more than one parent
class GrandParent:
    def land(self):
        print("Has Agriculture Land")    

class Father(GrandParent):
    def house(self):
        print("Has House")
        
class Mother():
    def gold(self):
        print("Has Gold")

class Son(Father, Mother):
    def car(self):
        print("Has Car")

son_obj = Son()
son_obj.land()
son_obj.house()
son_obj.gold()
son_obj.car()

# Hierarchal Inheritance : Multiple classes inheriting from a superclass
class GrandParent:
    def land(self):
        print("Has Agriculture Land")    

class Father(GrandParent):
    def house(self):
        print("Has House")
        
class Mother():
    def gold(self):
        print("Has Gold")

class Daughter(Father):
    def business(self):
        print("Has Business")

class Son(Father):
    def car(self):
        print("Has Car")

daughter_obj = Daughter()
daughter_obj.business()
daughter_obj.house()

#  Hybrid Inheritance : Combination of at least types types is called Hybrid
class A:
    def feat1(self):
        print("feature 1")

class B(A):
    def feat2(self):
        print("feature 2")

class C(A):
    def feat3(self):
        print("feature 3")
        
class D(B,C):
    def feat4(self):
        print("feature 4")

obj = D()
obj.feat1()
obj.feat2()
obj.feat3()
obj.feat4()