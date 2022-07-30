#BETA BETA BETA
from datetime import date
import calendar
import datetime 
from typing import TYPE_CHECKING
today = date.today()

m = int(input('Month: '))
d = int(input('Day: '))
y = int(input('Year: '))
age = today.year-y-((today.month, today.day)<(d,m))

fname = input ('Your name: ')

day_name = datetime.date(int(y),int(m),int(d))
    
h = float(input('Your Height in meters: '))
w = float(input('Your weight in kilogram: '))

BMI = w / (h**2)
BMI = round(BMI,2)


print('\nHi '+fname+'!')
print(f'You are {age} years old,')
print('the day you were born was a '+day_name.strftime('%A'))

if BMI <= 18.49:
    print('You\'re SKINNY because, your BMI is {:0.2f}'.format((BMI)))
elif BMI <= 24.99:
    print('You\'re Healthy! Your BMI is {:0.2f}'.format((BMI)))
elif BMI <= 29.99:
    print('You\'re getting FAT because your BMI is {:0.2f}'.format((BMI)))
elif BMI <= 34.99:
    print('You\'re FAT! Your BMI is {:0.2f}'.format((BMI)))
elif BMI <= 39.99:
    print('You\'re too FAT! Your BMI is {:0.2f}'.format((BMI)))
else:
    print('What\'s wrong with you!!! Your BMI is {:0.2f}'.format((BMI)))

while True:
    print('Do you want to proceed?: [y/n]')
    check = input()
    if check == 'n':
        break
    else:
        continue