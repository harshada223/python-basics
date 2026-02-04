import math
math.sqrt(4)
math.sqrt(60)
math.pi
print(math.sin(math.radians(90)))
print("________________________________________")

print("Data mmodules")
from datetime import date
print(date.today())
today=date.today()
print(today)
print(today.day, today.month, today.year)
print("________________________________________")

from datetime import datetime
print(datetime.now())
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  