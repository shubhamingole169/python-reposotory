# class Test:
#     @staticmethod
#     def add(a, b):
#         return a + b

# obj = Test()
# print(obj.add(2, 3))     # ✅ Works
# print(Test.add(2, 3))    # ✅ Also works directly with class name


# class Student:
#     school_name = "ABC School"   # Class Variable

#     @classmethod
#     def change_school_name(cls, new_name):
#         cls.school_name = new_name



# s = Student.change_school_name("xyz school")

# # print(s.school_name)
# s.school_name


# print(Student.school_name)        # Output: ABC School

# Student.change_school_name("XYZ School")

# print(Student.school_name)        # Output: XYZ School

# 
# @classmethod
# 

# class Employee:
#     company = "Apple"
    
#     def show(self):
#         print(f"my name is {self.name} and company name is {self.company}")
    
#     @classmethod
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany
        
        

# e1 = Employee()
# e1.name = 'shubham'

# e1.show()
# print(Employee.company)
# e1.changeCompany("tesla")
# e1.show()
# print(Employee.company)

# e2 = Employee()
# e2.name = 'xyz'

# e2.show()




# 
# Property Decorators (@property)
# 


# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     @staticmethod  # this wont working 
#     def radius(self):
#         return self._radius

#     @property
#     def area(self):
#         return 3.14 * (self._radius ** 2)

# c = Circle(5)
# print(c.radius)  # 5
# print(Circle.radius)   # this wont working
# print(c.area)    # 78.5

# 
# @property.setter
# 

# When you want to set or update the value of a property, you can control how it’s done using @property.setter.
# It helps you validate the new value or trigger some logic when someone tries to change it.

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
        
#     @property
#     def radius(self):
#         return self._radius
    
#     # @property
#     @radius.setter
#     def radius(self, new_radius):
#         if new_radius > 0:
#             self._radius = new_radius
#         else:
#             print("did you saw any negative radius in your life ??")
    
#     @property
#     def area(self):
#         return 3.14 * (self._radius ** 2)
    
    
    
    
# c = Circle(5)
# print(c.radius)     # 5
# print(c.area)       # 78.5
    
    
# c.radius = 10  # changing radius
# print(c.radius)     #10
# print(c.area)       #314.0

# c.radius = -5


# When you see self._radius (with underscore _ in front),
# it means:
# ➡️ "This is a private or internal variable. Please don't touch it directly from outside the class."

# ✅ Why we need _radius and not radius ?

# self.radius = new_radius

# inside the setter,
# then the setter will call itself again! (and again, and again... 🔥🔥 infinite loop!)

# ➡️ You are trying to set radius, but radius itself is managed by the setter.
# It will keep calling itself forever ➡️ crash!

# ➡️ You are trying to set radius, but radius itself is managed by the setter.
# It will keep calling itself forever ➡️ crash! 💥

# 
# 7. Decorators
# 

# Decorators are like "functions that modify other functions" without changing their original code.
# (Think of it like putting a filter on a photo 📸 — original photo stays same, but new look!)



# def decorator_function(orginal_function):
#     def wrapper_function():
#         print("wrapper executed before", orginal_function.__name__)
#         print("Before the function is called.")
#         orginal_function()
#         print("After the function is called.")
#     return wrapper_function


# @decorator_function
# def say_hello():
#     print("hellow next adorable person")
    
    
# say_hello()

# 💥 Another Example: Timing a Function

# import time

# def timer_decorator(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"Excution time: {end - start} seconds")
#     return wrapper

# @timer_decorator
# def slow_function():
#     time.sleep(2)
#     print("slow function finished.")
    


# slow_function()



# def decorator_function(original_function):
#     def wrapper_function():
#         print("Before the function is called.")
#         original_function()
#         print("After the function is called.")
#     return wrapper_function

# @decorator_function
# def say_hello():
#     print("Hello, world!")

# say_hello()




# 
# Decorators with arguments
# 


# What if your original function takes arguments?


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print("before")
#         original_function(*args, **kwargs)
#         print("after")
#     return wrapper_function


# @decorator_function
# def greet(name):
#     print(f"Hellow, {name} !!!")
    

# greet("Anokhi")


# @decorator_function is shortcut

# greet = decorator_function(greet)

# print(greet)



# Real-life Example: Authorization Check
# Imagine you have a website and some pages should be accessed only by logged-in users.

# Instead of adding login checks in every function, you can just decorate it!


# def login_required(func):
#     def wrapper(*args, **kwargs):
#         user_logged_in = True #suppose we checked user status
        
#         if user_logged_in:
#             return func(*args, **kwargs)
#         else:
#             print("for access this page login okay !!!")
#     return wrapper

# @login_required
# def view_profile():
#     print("here is your awsome profile !!!")
    
    
# view_profile()


# def repeat(n):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator

# @repeat(3)
# def say_hellow():
#     print("hellow beautiful world !!!")


# say_hellow()


# Simple formula to remember:

# decorator_maker --> actual_decorator --> wrapper --> function


def bold(func):
    def wrapper():
        return "<b>" + func() + "<b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper


@italic
@bold
def greet():
    return "Hellow !!!"

print(greet())
