#importing calendar module
import calendar
"""
yy = 2014  # year
mm = 11    # month
# display the calendar
print(calendar.month(yy, mm))

"""
"""
# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))
"""
#2nd type
# Program to display calendars for all months of a given year
# Input year from the user
yy = int(input("Enter year: "))

# Display the calendar for all months of the year
for mm in range(1, 13):
    # Print the month and year
    print(calendar.month_name[mm], yy)
    
    # Display the calendar for the current month
    print(calendar.month(yy, mm))
    print()

