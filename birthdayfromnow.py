import datetime
from datetime import date
today = date.today()


def print_header():
    print('------------------------------------------------')
    print('       BIRTHDAY CALC NI KITOY                   ')
    print('------------------------------------------------')
    print()

def get_birthday_from_user():

    month = int(input('Month: '))
    day = int(input('Day: '))
    year = int(input('Year: '))

    birthday = datetime.date(year, month, day)

    return birthday

def compute_days_between_dates(original_date, target_date):
    
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days

def print_birtday_information(days):

    FullName = input('Your name: ')
    print('Hi ' +FullName+'!',end='')
 
    if days < 0:
        print(' You had your birthday {} days ago.'.format(-days))
    elif days > 0:
        print(' Your birthday is in {} days!\n'.format(days))
    else:
        print(' Happy birthday!')

def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, now)
    print_birtday_information(number_of_days)

main()

while True:
    print('Do you want to continue? [y/n]: ',end='')
    check = input()
    if check == 'n' or check == 'N':
        print('\nThanks for visiting!\nHave a great day!\n')
        break
    else:
        main()