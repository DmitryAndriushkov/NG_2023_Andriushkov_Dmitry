from math import sqrt

print("\nHi! This is simple calculator in Python\nYou have this options:")
print("1) Addition\n2) Substraction\n3) Multiplication\n4) Division\n5) Square root of a number\n6) Exponentiation")

userChoise = input("Choose an option(number without brackets): ")

if userChoise == '5':
    num_SQRT = float(input("Your number: "))

else:
    firstNum = float(input("\nFirst number: "))
    secondNum = float(input("Second number: "))

match userChoise:
    case '1':
        print(f"\n{firstNum} + {secondNum} =",firstNum + secondNum)
    
    case '2':
        print(f"\n{firstNum} - {secondNum} =",firstNum - secondNum)
    
    case '3':
        print(f"\n{firstNum} * {secondNum} =",firstNum * secondNum)

    case '4':
        print(f"\n{firstNum} / {secondNum} =",firstNum / secondNum)

    case '5':
        print("\n{} is your result".format (sqrt(num_SQRT)))

    case '6':
        print(f"\nExponentiation result is",firstNum ** secondNum)