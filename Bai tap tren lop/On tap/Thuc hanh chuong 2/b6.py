while True:
    m = int(input('Enter m = '))
    if (1 <= m <= 12):
        break

y = int(input('Enter y = '))

isLeapYear = False

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    isLeapYear = True

dayInMonth = 31

if m == 2:
    dayInMonth = 29 if isLeapYear else 28
else:
    if m == 4 or m == 6 or m == 9 or m == 11:
        dayInMonth = 30

print(f'{m}/{y} of {dayInMonth} days')



