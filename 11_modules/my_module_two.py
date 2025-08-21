# This is my custom user defined module
name = "John"
email = "john@gmail.com"

def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def profile_info(name=name,email=email): # dynamic
    return f"Hi {name} you logged in with email {email}"