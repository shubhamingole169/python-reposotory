# What Are Regular Expressions?
# Regular expressions (regex) are patterns used to match character combinations in strings. Python provides this via the re module.



# 2. Common Functions
# | Function       | Purpose                                           |
# | -------------- | ------------------------------------------------- |
# | `re.search()`  | Searches for a pattern **anywhere** in the string |
# | `re.match()`   | Checks if pattern **starts** the string           |
# | `re.findall()` | Returns a list of all matches                     |
# | `re.sub()`     | Replaces parts of string                          |
# | `re.split()`   | Splits string by the pattern                      |

# 🔠 Regex Syntax Basics

# | Pattern | Matches                               |
# | ------- | ------------------------------------- |
# | `.`     | Any character except newline          |
# | `^`     | Start of string                       |
# | `$`     | End of string                         |
# | `*`     | 0 or more repetitions                 |
# | `+`     | 1 or more repetitions                 |
# | `?`     | 0 or 1 repetition                     |
# | `[]`    | Any one of the characters             |
# | `\d`    | Digit (0–9)                           |
# | `\D`    | Non-digit                             |
# | `\w`    | Word character (letters, digits, `_`) |
# | `\W`    | Non-word character                    |
# | `\s`    | Whitespace                            |
# | `\S`    | Non-whitespace                        |
# | `{n}`   | Exactly `n` times                     |
# | `{n,m}` | Between `n` and `m` times             |



import re

# text = "I love myself alot"
text = "I love Python 3.12"
match = re.search(r"Python \d\.\d+", text)

if match:
    print("Found: ", match.group())