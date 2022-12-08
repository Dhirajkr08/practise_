import calendar
from calendar import month, monthrange
year = int(input("enter a year"))
month = int(input("enter a month"))
days = monthrange(year,month)
print(days)