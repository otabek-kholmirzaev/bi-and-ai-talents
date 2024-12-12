"""

Write a program that checks if a string starts with one word and ends with another.
Example:

Input: "Python is fun!"
Starts with: "Python"
Ends with: "fun!"

"""

s = input("Input: ")
words = [w for w in s.split() if w]

print(f"Starts with: {words[0]}")
print(f"Ends with: {words[-1]}")