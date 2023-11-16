This program is a basic calculator implemented in Python. It allows the user to perform arithmetic operations, such as addition, subtraction, multiplication, division, and modulus. Additionally, it provides a feature to simplify mathematical expressions.

## Functions

The program utilizes the following functions:

- `add(numbers)`: This function takes a list of numbers as input and returns the sum of all the numbers.

- `subtract(numbers)`: This function takes a list of numbers as input and returns the result of subtracting all the numbers from the first number in the list.

- `multiply(numbers)`: This function takes a list of numbers as input and returns the result of multiplying all the numbers together.

- `divide(numbers)`: This function takes a list of numbers as input and returns the result of dividing the first number by the subsequent numbers in the list. It checks for division by zero and handles the error appropriately.

- `modulus(numbers)`: This function takes a list of numbers as input and returns the result of performing the modulus operation on the first number with the subsequent numbers in the list. It checks for performing the modulus operation with zero and handles the error appropriately.

- `simplify(expression)`: This function takes a mathematical expression as input and uses the `eval()` function to evaluate and simplify the expression. It handles errors such as division by zero or invalid expressions and returns appropriate error messages.

## Usage

1. The program prompts the user to select an operation by entering a choice from 1 to 6.
2. If the user selects option 6, they are prompted to enter a mathematical expression for simplification.
3. For options 1 to 5, the user is asked to enter numbers separated by spaces.
4. The program uses regular expressions (`re.findall()`) to extract numbers from the user's input and converts them to floating-point numbers.
5. Based on the user's choice, the appropriate function is called to perform the selected operation or simplify the expression.
6. The result of the operation or the simplified expression is displayed.

## Requirements

- Python 3.x
- re module (built-in)
