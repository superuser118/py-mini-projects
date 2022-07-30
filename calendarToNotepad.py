import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October', 'November',  'December')

print ('Calenday Maker')

while True:
    print ('Enter Calendar Year: ')
    response = input('> ')

    if response.isdecimal() and int (response) > 0:
        year = int (response)
        break

    print ('Please enter numeric value (i.e., 2022. ')
    continue

while True:
    print ('Enter Calendar month from 1 to 12. ')
    response = input('> ')

    if not response.isdecimal():
        print ('Please enter numeric value (i.e., 1 for January or 11 for November). ')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print ('Please enter numbers from 1 to 12. ')
    break

def getCalendayFor(year, month):
    calText = ''
    calText += (' ' * 34) + MONTHS [month - 1] + ' ' + str(year) + '\n'
    calText += '       SUN       MON       TUE        WED      THUR       FRI       SAT     \n'
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('|          ' * 7) + '|\n'
    currentdate = datetime.date(year, month, 1)

    while currentdate.weekday() != 6:
        currentdate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator
        
        daysNumberRow = ''
        for i in range(7):
            dayNumberLab = str(currentdate.day).rjust(2)
            daysNumberRow += '|' + dayNumberLab + (' ' * 8)
            currentdate += datetime.timedelta(days=1)
        daysNumberRow += '|\n'

        calText += daysNumberRow
        for i in range(3):
            calText += blankRow

        if currentdate.month != month:
            break
        
    calText += weekSeparator
    return calText

calText = getCalendayFor(year, month)
print (calText)

calFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calFilename,'w') as file0bj:
    file0bj.write(calText)

print ('Save to ' + calFilename)