import time
from datetime import date

# Dates and Times ===================================================================
now = date.today()
print(now)
# datetime.date(2003, 12, 2)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1979, 2, 28)
age = now - birthday
print(age.days)

time.sleep(0.5)
