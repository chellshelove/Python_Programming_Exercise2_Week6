# Get 5 integers from the user and store them in a list
numbers = [int(input(f"Enter integer {i+1}: ")) for i in range(5)]

# Print the maximum number
print("The maximum number is:", max(numbers))