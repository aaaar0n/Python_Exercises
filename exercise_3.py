#Write a Python program to display the current date and time.

import datetime

today = datetime.datetime.now()
print(today)
print(today.strftime('%Y-%m-%d %H:%M:%S'))
