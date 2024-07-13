# Check if Leap Year or not
year = int(input('Enter a Year :'))
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')

    