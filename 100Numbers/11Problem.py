# is Palindrome or not
num = int(input('Enter a number :'))
rev = 0
rem = 0
temp = num

while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10

if num == rev :
    print(f'{rev} is a palindrome')
else :
    print(f'{rev} is not a palindrome')
