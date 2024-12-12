# Write a program that takes three numbers and checks if all of them are different.

a = int(input())
b = int(input())
c = int(input())

print("All different" if a != b and b != c and c != a else "Not all different") 