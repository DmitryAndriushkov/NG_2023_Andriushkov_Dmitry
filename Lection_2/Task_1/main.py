
print("\nHi! This simple program can output unique elements")

userInput = int(input("Enter the number of elements you want: "))

uniqueElems = set()

for elems in range(userInput):
    strNum = input(f"[{elems + 1}] element: ")
    uniqueElems.add(strNum)

print("\nUnique elements:", list(uniqueElems))