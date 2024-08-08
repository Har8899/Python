# binary to decimal conversion
def convert_binary_to_decimal(binary):
    decimal = 0
    i = 0
    while binary != 0:
        digit = binary % 10
        decimal += digit * (2 ** i)
        binary //= 10
        i += 1
    return decimal

# Main function
if __name__ == "__main__":
    binary = int(input("Enter binary number: "))
    decimal_result = convert_binary_to_decimal(binary)
    print(decimal_result)

