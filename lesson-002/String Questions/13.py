# Ask the user for a string and remove all spaces from it.

s = input()

print("".join([c for c in s.split() if c]))