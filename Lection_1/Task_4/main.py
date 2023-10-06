from math import sqrt

print("\nHi! This is simple calculator in Python\nYou have this options:")
print("1) Addition\n2) Substraction\n3) Multiplication\n4) Division\n5) Square root of a number\n6) Exponentiation")

userChoise = input("Choose an option(number without brackets): ")

match userChoise:
    case '1' | '2' | '3' | '4' | '6':
        firstNum = float(input("\nFirst number: "))
        secondNum = float(input("Second number: "))

    case '5':
        num_SQRT = float(input("Your number: "))

    case _:
        print("\nError! Wrong number, please choose a correct number(1-6)")
        exit()

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