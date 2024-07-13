# Reverse number part 2
num = -1234


def rev(num):
    if num < 0:
        num = str(abs(num)) + '-'
    return int(str(num)[::-1])


print(rev(num))
