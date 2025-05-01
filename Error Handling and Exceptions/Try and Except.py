# Error Handling and Exceptions in Python
# In Python, errors are called exceptions, and they can be managed using try, except, else, and finally blocks.

# Why is error handling important?

# It helps prevent the program from crashing when an error occurs.

# It allows you to handle different types of errors gracefully.

# 1. Try and Except

# The most common way to handle errors is by using the try and except blocks.


# try:
#     num = int(input("Enter a number: "))
#     print(f"The number is: {num}")
# except ValueError:
#     print("Opps ! you really think that was a number ?? ")
    
    
# In this example:

# The try block contains code that might raise an exception.

# The except block catches and handles the exception, in this case, a ValueError (if the user doesn't input a valid number).


# 2. Multiple Except Blocks

# You can have multiple except blocks to handle different types of errors

# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print(f"Result: {result}")
# except ValueError:
#     print(f"You really think with this you can devide ??")
# except ZeroDivisionError:
#     print("yaar you cant divide any number with 0 (zero) !!!")

# 3. Else Block
# You can use the else block if you want to run code that should execute only if the try block does not raise an exception.


# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("You really want o devide with it ??")
# except ZeroDivisionError:
#     print("yaar its zero we cant devide with this !!!!")
# else:
#     print(f"Results : {result}")


# 4. Finally Block
# The finally block is used to execute code that must run no matter what, whether an exception is raised or not.

# try:
#     num = int(input("Enter a number : "))
#     result = 10 / num
# except ValueError:
#     print("its not number i guess !!!")
# except ZeroDivisionError:
#     prin("its zero !!!")
# else:
#     print(f"Result: {result}")
# finally:
#     print("This will always run, no matter what !!!")



# 5. Raising Exceptions
# You can also raise exceptions manually using the raise keyword.

# def check_age(age):
#     if age < 18:
#         raise ValueError("Age must be 18 or above !!!")
#     print(f"Age is {age}")
    

# try:
#     check_age(16)
# except ValueError as e:
#     print(f"Error: {e}")


# 6. Custom Exceptions
# You can define your own exception classes by inheriting from Python's built-in Exception class.

# class AgeError(Exception):
#     pass


# def check_age(age):
#     if age < 18:
#         raise AgeError("Age must be 18 or above !!!")
#     print(f"Age is {age}")

# try:
#     check_age(14)
# except AgeError as e:
#     print(f"Custom Error: {e}")