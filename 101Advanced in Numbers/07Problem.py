# octal to decimal
def convert_to_decimal(octal):
    decimal = 0
    i = 0
    base = 8

    while octal != 0:
        digit = octal % 10
        decimal += digit * pow(base, i)
        octal //= 10
        i += 1

    return decimal


# Main function
if __name__ == "__main__":
    octal = int(input("Enter octal number: "))
    print("Decimal equivalent:", convert_to_decimal(octal))
