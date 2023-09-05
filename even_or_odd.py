# option 1:
'''
def even(number):
    try:
        return int(number) % 2 == 0
    except ValueError:
        return False
    

user_input = input("Enter a number: ")

if is_even(user_input):
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is not an even number.")
'''
# option 2 one digit;
'''
num = input("Enter a value")

for digit in num:
    digit = int(digit)  # Convert the digit to an integer
    if digit % 2 == 0:
        print(f"{digit} is Even")
    else:
        print(f"{digit} is Odd")
'''
#option 3
'''
num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
'''
# option 4
'''
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

'''
#option 5(only even or odd)
'''
num = input("Enter a value")

for digit in num:
    digit = int(digit)  # Convert the digit to an integer
    if digit % 2 == 0:
        print(digit)

'''
#option 6
'''
for number in range(101):  # Range from 0 to 100 (inclusive)
    if number % 2 == 0:
        print(f"Even: {number}")
    else:
        print(f"Odd: {number}")
'''
#option 7
num = input("Enter a value")

for digit in num:
    digit = int(digit)  # Convert the digit to an integer
    if digit % 2 == 0:
        print(digit)

