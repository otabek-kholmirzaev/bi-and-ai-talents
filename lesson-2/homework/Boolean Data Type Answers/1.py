# Write a program that accepts a username and password and checks if both are not empty.

username = input()
password = input()

print("username is not empty" if username else "username is empty")
print("password is not empty" if password else "password is empty")