
print("\nHi! This simple program can output unique elements")

userInput = int(input("Enter a value of elements you want: "))

userElems = []
uniqueElems = []

for elems in range(userInput):
    strNum = input(f"[{elems + 1}] element: ")
    userElems.append(strNum)
    if strNum not in uniqueElems:
        uniqueElems.append(strNum)

print("Your elements: ", userElems)
print("Unique elements: ", uniqueElems)