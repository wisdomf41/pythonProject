# This calculator will collect three inputs from users and perform the basic mathematical operations
# It will calculate +, -, /, *

num = float(input("Enter a number: "))
op = input("Enter an Operator: ")
num1 = float(input("Enter another number: "))
if op == "+":
     print(num + num1)
elif op == "-":
    print(num - num1)
elif op == "/":
    print(num / num1)
elif op == "*":
    print(num * num1)
else:
    print("Invalid operator")
