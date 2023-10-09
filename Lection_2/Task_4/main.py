
print("\nHi! This program can output vowels letters of your string")

userInput = input("\nWrite your string: ")

lettersLst = []
vowLetters = ('A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y')

for letter in userInput:
    if letter in vowLetters not in lettersLst:
        lettersLst.append(letter)

print("\nAmount of vowels letters in string: ", len(lettersLst))
print("List of vowels letters: ", sorted(lettersLst))