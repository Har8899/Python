#

# Function to calculate the number of digits in a number
def order(num):
    return len(str(num))


# Function to check if a number is an Armstrong number
def armstrong(num, length):
    temp = num
    sum = 0

    while temp != 0:
        digit = temp % 10
        sum += digit ** length
        temp //= 10

    return sum == num


num = int(input("Enter a number: "))
length = order(num)

if armstrong(num, length):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
