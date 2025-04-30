# ➔ Generators
# Generators are special functions that allow you to generate values one at a time, instead of creating the whole list at once.
# (Kind of like a lazy list.)


# def my_generator():
#     yield 1
#     yield 2
#     yield 3
    
# gen = my_generator()

# print(next(gen)) # 1
# print(next(gen)) # 2
# print(next(gen)) # 3

# Instead of using return, we use yield.
# Every time we call next(), it gives the next value.


# 🎯 What are Generators in Python?
# Generators are special functions that do not return all results at once.

# Instead, they yield values one by one only when asked (using next()).

# This saves memory and makes code faster, especially for large datasets.

#  How to Create a Generator?
# ✅ A function becomes a generator if it uses yield instead of return.

# Example:


# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
    

# gen = simple_generator()

# print(next(gen))   # Output: 1
# print(next(gen))   # Output: 2
# print(next(gen))   # Output: 3
# # print(next(gen)) # Output: StopIteration error

# 🎯 Why Use Generators?
# ✅ Memory efficient:
# Imagine you need a list of 1 billion numbers.
# If you use a normal list → your RAM will cry. 😭
# But with a generator, it creates one number at a time = lightweight.

# ✅ Faster startup:
# You can start processing even before the full sequence is ready.

# ✅ Easy to read and write:
# Cleaner code compared to creating big lists manually.


# Normal list approach: 👆 This takes a lot of memory!

# def creat_list(n):
#     result = []
#     for i in range(n):
#         result.append(i)
#     return result

# lst = creat_list(1000000)


# Generator approach:

# def create_number(n):
#     for i in range(n):
#         yield i

# gen = create_numbers(100000)

# Here, gen will produce numbers one by one on demand.

# No heavy memory use! ✨


# def square_numbers(nums):
#     for num in nums:
#         yield num * num
        
# gen = square_numbers([1, 2, 3, 4, 5])

# for i in gen:
#     print(i)


# numbers = [x * 2 for x in range(5)]
# print(numbers)
# # Output: [0, 2, 4, 6, 8]

# numbers = (x * 2 for x in range(5))
# print(numbers)
# # Output: <generator object ...>

# for num in numbers:
#     print(num)
# # Output:
# # 0
# # 2
# # 4
# # 6
# # 8



# # Create a generator expression to find even numbers from 1 to 1 million
# even_numbers = (x for x in range(1, 1000001) if x % 2 == 0)

# # Loop through the generator and print the first 10 even numbers
# for i, num in enumerate(even_numbers):
#     if i == 10:
#         break
#     print(num)







