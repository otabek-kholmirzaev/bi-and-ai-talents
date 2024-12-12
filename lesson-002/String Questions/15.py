"""

Ask the user for a sentence and create an acronym from the first letters of each word.
Example:

Input: "World Health Organization"
Output: "WHO"

"""

s = input()
print("".join([w[0] for w in s.split() if w]))