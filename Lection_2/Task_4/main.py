
print("\nHi! This program can output vowel letters of your string")

userInput = input("Write your string: ")

lettersLst = []
vowLetters = "aeiouy"

for letter in userInput.lower():
    if letter in vowLetters:
        lettersLst.append(letter)

print("\nList of vowel letters:", sorted(lettersLst))