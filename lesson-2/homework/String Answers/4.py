"""
    4. Write a Python program to check if a given string is palindrome or not.
        - What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
"""

s = input()

print("Palindrome" if s == s[-1::-1] else "Not palindrome")