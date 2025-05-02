# What is a Class?
# A class is like a blueprint for creating objects. It defines:

# What data the object should have (attributes)

# What it can do (methods)


# 🔹 What is an Object?
# An object is an instance of a class — like how you can create many cars (objects) from one car blueprint (class).

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hellow, I'm {self.name} and i'm {self.age} year old.")


s1 = Student("Alice", 20)
s2 = Student("shubham",24)

s1.greet()
s2.greet()