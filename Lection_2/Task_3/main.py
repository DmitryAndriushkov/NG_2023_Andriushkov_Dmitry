
print("\nHi! This program can:\n 1)Display numbers from 1 to the number specified by user\n 2)Display natural numbers from the first column\n 3)Display prime numbers")

userInput = int(input("\nEnter your number: "))
primeNumber = []

for nums in range(1, userInput+1):
    zeroDivider = set()
    
    for dividerNums in range(1, nums+1):
        if nums % dividerNums == 0:
            zeroDivider.add(dividerNums)
    print(f"   {nums}   ->   {zeroDivider}")

    if len(zeroDivider) == 2:
        primeNumber.append(nums)

print("Prime numbers from the first column")
for prime in primeNumber:
    print(f"{prime}")