
print("1) Convert Celsius to Fahrenheit")
print("2) Convert Fahrenheit to Celsius")

userChoice = input("Please choose an option (1 or 2): ")

if userChoice == '1':
    celsius = float(input("Enter degrees in Celsius: "))
    print(f"{celsius} degrees Celsius is {celsius * 9/5 + 32} degrees Fahrenheit")

elif userChoice == '2':
    fahrenheit = float(input("Enter degrees in Fahrenheit: "))
    print(f"{fahrenheit} degrees Fahrenheit is {(fahrenheit - 32) * 5/9} degrees Celsius")

else:
    print("Invalid choice. Please choose 1 or 2")