# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Validate the input to ensure it's a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Use a while loop to iterate through each row of the pattern
    row = 0
    while row < size:
        # Inside the while loop, use a for loop to print asterisks
        for _ in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        row += 1