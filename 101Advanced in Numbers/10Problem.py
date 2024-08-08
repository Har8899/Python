# decimal to octal
def convert_to_octal(num):
    octal_array = []

    while num > 0:
        octal_array.append(num % 8)
        num //= 8

    for digit in reversed(octal_array):
        print(digit, end="")


# Main function
if __name__ == "__main__":
    n = 11
    print("Octal equivalent:", end="")
    convert_to_octal(n)
