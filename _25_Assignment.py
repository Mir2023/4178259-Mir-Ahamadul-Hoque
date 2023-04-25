'''
You can write :
from datetime import datetime
from datetime import date
from datetime import time
'''


'''
from datetime import date, datetime
day = int(input('Enter a day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))
d = date(year, month, day)
print(d)
from datetime import datetime
birth_date = datetime(1987,5,30).date()
print(birth_date)
if d == birth_date:
    print("Its your birth date.")
else:
    print("Sorry. Its not your birth date.")
print('------------------1----------------------')
from datetime import date, datetime   # YOU CAN IMPORT MULTIPLE KEYWARD
day = int(input('Enter a day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))
d = date(year, month, day)

birth_date = datetime(1987,5,30).date()


if d == birth_date:
    print("Its your birth date.")
else:
    print("Sorry. Its not your birth date.")
print('------------------2---------------------')
'''
# FINAL
from datetime import date, datetime   # YOU CAN IMPORT MULTIPLE KEYWARD
day = int(input('Enter a day: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))
try:
    d = date(year, month, day)
    print(d.strftime("%d/%m/%y"))
    birth_date = datetime(1988,5,30).date()
    print(birth_date.strftime("%d/%m/%y"))

    if d == birth_date:
        print("Its your birth date.")
    else:
        print("Sorry. Its not your birth date.")
except Exception as ex:
    print("Input data correctly.")