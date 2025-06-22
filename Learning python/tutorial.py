num1 = float(input("Enter your number: "))
op = input("Enter your desired operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        result = "cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "invalid operator"
print(f"Result: {result}")
