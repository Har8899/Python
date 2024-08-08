# hexadecimal to decimal
def convert_to_decimal(hexadecimal):
    decimal = 0
    pos = 0
    for char in hexadecimal[::-1]:
        if char.isdigit():
            digit = int(char)
        else:
            digit = ord(char.upper()) - ord('A') + 10
        decimal += digit * (16 ** pos)
        pos += 1
    return decimal

# Main function
if __name__ == "__main__":
    hex_input = input("Enter hexadecimal number: ")
    print("Decimal equivalent:", convert_to_decimal(hex_input))
