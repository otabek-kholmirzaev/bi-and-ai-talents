# Create a program to ask name and year of birth from user and tell them their age.

name = input("Your name: ")
year = int(input("Your birth year: "))
age = 2024 - year

print(f"{name}, your're {age} years old.")