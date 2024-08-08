# Armstrong no. in a range
# Function to calculate the number of digits in a number
def order(num):
    len = 0
    while num:
        len += 1
        num = num // 10
    return len


# Function to find and print Armstrong numbers in a given range
def armstrong(low, high):
    count = 0
    for num in range(low, high + 1):
        sum = 0
        temp, digit, len = num, 0, 0
        len = order(num)

        temp = num
        while temp != 0:
            digit = temp % 10
            sum += digit ** len
            temp //= 10

        if sum == num:
            print(num, end=' ')
            count += 1

    if count == 0:
        print("Given Range does not have any Armstrong numbers.")


# Main function
if __name__ == "__main__":
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the high bound: "))

    print(f"Armstrong numbers between {low} and {high} are: ", end='')
    armstrong(low, high)
