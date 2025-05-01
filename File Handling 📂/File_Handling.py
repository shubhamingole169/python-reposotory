

# #writing into a file

# with open("sample.txt", "w") as file:
#     file.write("hellow, this is the first line!\n")
#     file.write("and this is second line.\n")
    
# #Appending into a file
# with open("sample.txt", "a") as file:
#     file.write("This is a new line added later!\n")

    

# #reading from the file

# # with from the same file

# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
#     print(file.read())
#     print()




# 📖 1. "r" — Read Mode
# Only reading, no writing!

# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)
    
    
#     # If the file doesn’t exist, it gives an error.

# # You cannot write anything in this mode.


# ✍🏻 2. "w" — Write Mode
# Write new data — BUT be careful, it deletes old content!

# with open("sample.txt", "w") as file:
#     file.write("Hellow, this is new data !!!")
    
# # If file exists → erase everything inside first.

# # If file doesn't exist → create new file.


# ➕ 3. "a" — Append Mode
# Safely add new content to bottom, without deleting anything.

# with open("sample.txt", "a") as file:
#     file.write("\nAnother line added")

# Useful for logs, notes, saving user data, etc.

#  4. "r+" — Read and Write Mode
# Read old content + also modify/write if needed.

# with open("sample.txt", "r+") as file:
#     file.write("\nAddidng new line after reading!!!.")
#     content = file.read()
#     print(content)


# file = open("sample.txt", "r")
# content = file.read()
# print(content)
# file.close()

# Normally, when we open a file, we should always close it manually after finishing.
# Example without with:

# if you forget file.close(), the file stays open in memory 😬 → can cause memory leak or file locking issues.

# ✅ But when you use with open,
# Python automatically closes the file when you exit the block!


# copy image using binary mode

with open("original.jpg", "rb") as original_file:
    data = original_file.read()
    

with open("copy.jpg", "wb") as copy_file:
    copy_file.write(data)
    

print("Image copy successfully !!!")


# Copy image using binary mode

# with open("original.jpg", "rb") as original_file:
#     data = original_file.read()

# with open("copy.jpg", "wb") as copy_file:
#     copy_file.write(data)

# print("Image copied successfully ✅")
