import random
from datetime import date

today = date.today()

print ("\nKitoy\'s  P O W E R  L O T T O ! ")
print ('\npress any key to continue.')

#print ('Please confirm your age.')

#print ('Format must be MM/DD/YYYY or 12 03 1989.')
#m = int(input('Month: '))
#d = int(input('Day: '))
#y = int(input('Year: '))

#age = today.year-y-((today.month, today.day)<(d,m))

#if age <= 18:
    #print ('You need to be 18.')
    #print ('Do you still wan\'t to play?: [Y/N]')
    
while True:
    check = input()
    if check == 'n' or 'N':
        break

while True:
    print ("\nPlease enter number 5 different numbers from 1 to 69 with spaces between. ")
    print ("For example: 5, 15, 27, 35, 50")
    response = input('> ')

    numbers = response.split()
    if len(numbers) !=5:
        print ("Please enter 5 different numbers with space between")
        continue

    try:
        for i in range(5):
            numbers[i] = int(numbers[i])
    except ValueError:
        print ("Please enter numbers like 24, 37 or 66.")
        continue

    for i in range(5):
        if not (1 <= numbers [i] <= 69):
            print ("The numbers must all be between 1 and 69.")
            continue

    if len (set(numbers)) != 5:
        print ("You must enter 5 different numbers.")
        continue

    break

while True:
    print ('Enter the Power LOTTO number from 1 to 26. ')
    response = input('> ')

    try:
        powerlotto = int(response)
    except ValueError:
        print ('Please enter number like 3, 15, or 22. ')
        continue

    if not (1 <= powerlotto <= 26):
        print ('You can play between 1 and 26.')
        continue

    break
while True:
    print ('How many times do you wan\'t to play? (MAX: 1000000)')
    response = input('> ')

    try:
        numPlays = int(response)
    except ValueError:
        print ('Please enter a number like 3, 15, or 22000.')
        continue

    break

price = '$' + str(2 * numPlays)
print ('It cost', price, 'to play', numPlays, 'times, but don\'t')
print ('worry. You\'ll win it all back. ')
input ('Press ENTER to start...')

possibleNumbers = list (range(1, 70))
for i in range(numPlays):
    random.shuffle(possibleNumbers)
    winningNumbers = possibleNumbers[0:5]
    winningPowerlotto = random.randint(1, 26)

    print ('Winning numbers are: ', end='')
    allWinningNums = ''
    for i in range(5):
        allWinningNums += str(winningNumbers[i]) + ' '
    allWinningNums += 'and' +' ' + str(winningPowerlotto)
    print (allWinningNums.ljust(21), end='')

    if (set(numbers) == set(winningNumbers) and powerlotto == winningPowerlotto):
        print ()
        print ('Congratulations! You have won the KITOY\'s POWERLOTTO!')
        break
    else:
        print ('Sorry you lost.')
        print ('You wasted ', price)
        print ('Thanks for playing!')