import re


def add(numbers):
    return sum(numbers)


def subtract(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result -= numbers[i]
    return result


def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


def divide(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] != 0:
            result /= numbers[i]
        else:
            return "Error: Cannot divide by zero!"
    return result


def modulus(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] != 0:
            result %= numbers[i]
        else:
            return "Error: Cannot perform modulus operation with zero!"
    return result


def simplify(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except Exception as e:
        return "Error: Invalid expression!"


print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Simplify")

choice = input("Enter choice (1-6): ")

if choice == '6':
    expression = input("Enter a mathematical expression: ")
    result = simplify(expression)
else:
    numbers = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+",
                         input("Enter numbers separated by space: "))
    numbers = [float(num) for num in numbers]

    if choice == '1':
        result = add(numbers)
    elif choice == '2':
        result = subtract(numbers)
    elif choice == '3':
        result = multiply(numbers)
    elif choice == '4':
        result = divide(numbers)
    elif choice == '5':
        result = modulus(numbers)
    else:
        result = "Invalid input!"

print("Result:", result)
