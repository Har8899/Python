# Prime factorisation
import math

def prime_factors(num):
    while num % 2 == 0:
        print(2, end=" ")
        num = num // 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            print(i, end=" ")
            num = num // i

    if num > 2:
        print(num, end=" ")

# Main function
if __name__ == "__main__":
    num = 1716
    print("Prime factors of", num, "are:", end=" ")
    prime_factors(num)
