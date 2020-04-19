import math

splitInput = userInput.split()
splitInput[1]

num1 = float(splitInput[0])
num2 = float(splitInput[2])
character = splitInput[1]

if character == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif character == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif character == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif character == "/":
    print(num1, "/", num2, "=", num1 / num2)
elif character == "**":
    print(num1, "**", num2, "=", num1 ** num2)
elif character == "r":
    print(num1, "root", num2,
            "=", num2 ** (1 / num1))
elif character == "%":
    print(num1, "%", num2, "=", num1 % num2)
#factorial
elif character == "!":
    theNumber = num1 = num2
    num2 = 1
    while num1 > 1:
        num2 *= num1
        num1 = num1 - 1
    print("n!(", theNumber, ")=", num2)
elif character == "sin":
    print("sin(", num2, ")=", math.sin(num2))
elif character == "cos":
    print("cos(", num2, ")=", math.cos
            (num2))
elif character == "tan":
    print("tan(", num2, ")=", math.tan(num2))
elif character == "pie" or character == "pi":
    print("Pie =", math.pi)
elif character == "e":
    print = ("E =", math.e)
elif character == "ln":
    print("ln(", num2, ")= ", math.log(num2))
