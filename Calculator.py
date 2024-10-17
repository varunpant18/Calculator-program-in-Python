# Python calculator

operator = input("Enter an operator(+, -,  *, /): ")
num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the Second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not the valid operator")