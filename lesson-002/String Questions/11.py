# Write a program to check if a string contains any digits.

s = input()

contains = False
for c in s:
    if c in '0123456789':
        contains = True
        break

print("YES" if contains is True else "NO")