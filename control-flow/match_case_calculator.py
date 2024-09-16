# Prompt the user for the first number
num1 = float(input("Enter the first number: "))

# Prompt the user for the second number
num2 = float(input("Enter the second number: "))

# Prompt the user for the operation they would like to perform
operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform the calculation using Match Case
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()  # Exit the program if division by zero is attempted
        else:
            result = num1 / num2
    case _:
        print("Invalid operation.")
        exit()  # Exit the program if the operation is invalid

# Output the result
print(f"The result is {result}.")