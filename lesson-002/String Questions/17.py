# Ask the user for a string and replace all the vowels with a symbol (e.g., *).

s = input()
for v in 'aeiou':
    s = s.replace(v, '*')

print(s)