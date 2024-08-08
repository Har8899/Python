# decimal to hexadecimal

def convert_to_hexadecimal(num):
    hexadecimal = ""
    while num != 0:
        rem = num % 16
        if rem < 10:
            hexadecimal = chr(rem + 48) + hexadecimal
        else:
            hexadecimal = chr(rem + 55) + hexadecimal
        num = num // 16
    return hexadecimal

# Main function
if __name__ == "__main__":
    decimal = 1456
    hexadecimal_result = convert_to_hexadecimal(decimal)
    print("Hexadecimal equivalent:", hexadecimal_result)
