# 12. Write a Python program that prints the calendar for 
# a given month and year.
# Note : Use 'calendar' module.

import calendar
m = int(input("Input month: "))
y = int(input("Input year: "))
print(calendar.month(y, m))
