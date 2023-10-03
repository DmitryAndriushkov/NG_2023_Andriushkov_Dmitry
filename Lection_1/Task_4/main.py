from math import sqrt

print("\nHi! This is simple calculator in Python\nYou have this options:")
print("1) Addition\n2) Substraction\n3) Multiplication\n4) Division\n5) Square root of a number\n6) Exponentiation")

userChoise = input("Choose an option(number without brackets): ")


match userChoise:
    case '1':
        firstNum = float(input("\nFirst number: "))
        secondNum = float(input("Second number: "))
        result_1 = (firstNum + secondNum)
       
        print(f"{firstNum} + {secondNum} = {result_1}\n")
    
    case '2':
        firstNum = float(input("\nFirst number: "))
        secondNum = float(input("Second number: "))
        result_2 = (firstNum - secondNum)
       
        print(f"{firstNum} - {secondNum} = {result_2}\n")
    
    case '3':
        firstNum = float(input("\nFirst number: "))
        secondNum = float(input("Second number: "))
        result_3 = (firstNum * secondNum)
        
        print(f"{firstNum} * {secondNum} = {result_3}\n")

    case '4':
        firstNum = float(input("\nFirst number: "))
        secondNum = float(input("Second number: "))
        result_4 = (firstNum / secondNum)
        
        print(f"\n{firstNum} / {secondNum} = {result_4}")

    case '5':
        num_SQRT = float(input("Your number: "))
        result_5 = (sqrt(num_SQRT))
       
        print(f"{result_5} is your result\n")

    case '6':
        firstNum = float(input("\nFirst number: "))
        secondNum = float(input("Exponentiation number: "))
        result_6 = (firstNum ** secondNum)

        print(f"Exponentiation result is {result_6}\n")