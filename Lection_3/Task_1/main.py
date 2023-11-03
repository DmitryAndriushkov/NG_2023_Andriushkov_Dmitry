
print("\nHi! This program can accept the file name to be processed and shows the number of characters and the number of each character separately(works on any language)")

userFileName = input("Enter your path to the file: ")
charVocabulary = {}

with open(userFileName, encoding='utf-8') as file:
    readFile = file.read()
    
    for char in readFile:
        charVocabulary[char] = charVocabulary.get(char, 0) + 1

print(f"Amounts of every character in your file: \n\n{charVocabulary}\n")