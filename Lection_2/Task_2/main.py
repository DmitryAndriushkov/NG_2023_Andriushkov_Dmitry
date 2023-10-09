
print("\nHi! This program can output only numbers of your list")

userInput = int(input("Enter a value of elements you want: ",))

userElems = []

for elems in range(userInput):
    strNum = input(f"[{elems + 1}] element: ")
    userElems.append(strNum)

lstOfNumbers = [elem for elem in userElems if elem.isdigit()]

if lstOfNumbers:
    print("\nNumbers in your list: ", lstOfNumbers)
    print("Amount of numbers in your list: ", len(lstOfNumbers))
else:
    print("No numbers found in your list!")