"""
Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.

Example:
    Input sentence: "I love apples."
    Replace: "apples"
    With: "oranges"
    Output: "I love oranges."
"""

sentence = input("Input sentence: ")
_replace = input("Replace: ")
_with = input("With: ")

print(sentence.replace(_replace, _with))