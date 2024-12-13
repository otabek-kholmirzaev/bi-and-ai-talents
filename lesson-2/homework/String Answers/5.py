# 5. Write a program that counts the number of vowels and consonants in a given string.

s = input()

vowels = 0
consonants = 0

for c in s:
    if c in 'aeiou':
        vowels += 1
    else:
        consonants += 1

print(f"vowels count: {vowels}")
print(f"consonants count: {consonants}")