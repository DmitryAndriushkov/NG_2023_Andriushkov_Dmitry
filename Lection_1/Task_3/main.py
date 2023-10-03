
print("\nHi! This program can:")
print("1) Convert Celsius to Fahrenheit\n2) Convert Fahrenheit to Celsius")

userChoise = input("\nPlease choose an option(number without brackets): ")

if userChoise == '1':
    ceslsius_num = float(input("Enter degrees in Celsius: "))
    result_FAHR = (ceslsius_num * (9/5) + 32)
    print(f"\nYour result is {result_FAHR} degrees Fahrenheit")

elif userChoise == '2':
    fahrenheit_num = float(input("Enter degrees in Fahrenheit: "))
    result_CEL = ((fahrenheit_num - 32) * 5/9)
    print(f"\nYour result is {result_CEL} degrees Celsius")

else:
    print("Wrong number. Please choose a number without brackets(1 or 2)!!!\n")