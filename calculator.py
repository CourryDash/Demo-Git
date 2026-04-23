print("Welcome to Calculator")
def add(a,b):
    return a + b

def subtraction(a, b):
    return a - b

def multiply(a,b):
    return a*b

print(add(10,5))
print(subtraction(10, 5))

def divide(num1, num2):
    if num2 != 0:
        pembagian = num1 / num2
        return pembagian
    else:
        return "Error: Division by zero is not allowed."