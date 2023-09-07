'''
for i in range(1, 11):  # This outer loop iterates from 1 to 10
    print(f"Multiplication Table for {i}:")

    for j in range(1, 11):  # This inner loop iterates from 1 to 10 for each number in the outer loop
        result = i * j
        print(f"{i} x {j} = {result}")

    print()  # Add a blank line after each table for better readability
'''
for i in range(1, 101):
    for j in range(1, 101):
        result = i * j
        print(result, end="\t")  # Use tab as a separator
    print()  # Move to the next line after each row
