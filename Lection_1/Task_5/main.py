from math import sqrt

print("\nHi! This program can solve quadratic equation by using Discriminant")
print("ax² + bx + c = 0\n\nD = b² - 4ac")

dA = float(input("\n'a' number: "))
dB = float(input("'b' number: "))
dC = float(input("'c' number: "))
Discriminant = ((dB**2) - 4 * dA * dC)

if Discriminant > 0:
    x1 = (-dB + sqrt(Discriminant)) / (2 * dA)
    x2 = (-dB - sqrt(Discriminant)) / (2 * dA)
    print(f"Roots of this quadratic equation are x1 = {x1}, x2 = {x2}")

elif Discriminant == 0:
    x = (-dB) / 2 * dA
    print(f"There is just one root x = {x}")

elif Discriminant < 0:
    imaginariusNum = sqrt(abs(Discriminant))
    x1I = (-dB + imaginariusNum) / (2 * dA)
    x2I = (-dB - imaginariusNum) / (2 * dA)
    print(f"Roots of negative Discriminant are x1 = {x1I} + i, x2 = {x2I} - i")