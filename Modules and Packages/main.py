# import mymodule

# print(mymodule.greet("shubham"))
# print(mymodule.pi)


# import calculator

# print(calculator.add(10, 5))
# print(calculator.multiply(3, 4))


# import math
# import random

# print(math.sqrt(25))
# print(random.randint(1,1000000))

# import datetime

# now = datetime.datetime.now()
# print("Current Date and Time:", now)

# print("year: ", now.year)
# print("Month: ", now.month)
# print("Day: ", now.day)


# print("Formatted :", now.strftime(" %d-%m-%Y %H:%M:%S"))


# import time

# print("Wait for 3 seconds ...")
# time.sleep(10)
# print("done waiting ...")


# import os

# print("current Direcory: ", os.getcwd())
# print("List file:", os.listdir())


# os.mkdir("new_folder")


# sys – Access System Info and Arguments

# import sys

# print("Python version: ", sys.version)
# print("\nPlatform: ", sys.platform)

# print("Command-line args:", sys.argv)


#  5. json – Work with JSON (used in APIs and config)

# import json

# data = '{"name": "Alice", "age": 25}'

# parsed = json.loads(data)

# print(parsed["name"])

# json_string = json.dumps(parsed)
# print(json_string)

# import json

# data = '{"name": "Alice", "age": 25}'
# parsed = json.loads(data)   # Convert JSON string to dictionary

# print(parsed["name"])       # Output: Alice

# # # Convert back to JSON
# # json_string = json.dumps(parsed)
# # print(json_string)


# 📌 1. json.loads() – JSON string → Python dict

# import json

# data = '{"name":"alice", "age":25}'
# parsed = json.loads(data)
# print(parsed)
# print(parsed['name'])


# 📌 2. json.dumps() – Python dict → JSON string

# import json

# person = {'name':'bob', 'age':30}
# json_string = json.dumps(person)

# print(json_string)


# 📁 3. json.load() – Read JSON from a file


# import json

# with open('data.json', 'r') as file:
#     parsed = json.load(file)
#     print(parsed)


import json

info = {"language": "Python", "version":3.11}

with open('output.json', 'w') as file:
    json.dump(info, file)
    
with open('output.json', 'r') as file:
    x = json.load(file)
    print(x)