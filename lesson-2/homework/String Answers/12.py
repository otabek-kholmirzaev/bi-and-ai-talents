# Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).

s = input()

words = s.split(',')

print("".join(words))