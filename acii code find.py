# Program to find the ASCII value of the given character
import random
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))
print(chr(68))
for i in range(0,20):
    a=random.randint(1,100)
    print(chr(a),end='')

print()

# Generate and display 30 unique random ASCII values
d = random.sample(range(32, 127), 30)
# ASCII values between space and tilde (~)

for ascii_value in d:
    print(chr(ascii_value), end=' ')

print()  # Print a newline at the end for better formatting
    
