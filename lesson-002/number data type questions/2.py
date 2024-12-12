# Write a Python file that asks for three numbers and outputs the largest and smallest.

a = int(input())
b = int(input())
c = int(input())

print(min(a, min(b, c)))
print(max(a, max(b, c)))