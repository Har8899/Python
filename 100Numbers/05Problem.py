# Prime numbers or not Part 1
isprime = True
n = 10

if n < 2:
    isprime = False

else:
    x = n // 2
    for i in range(2,x+1):
        if n % i == 0:
            isprime = False
            break

if isprime:
    print(f'{n} is a prime number ')
else:
    print(f'{n} is not a prime number')