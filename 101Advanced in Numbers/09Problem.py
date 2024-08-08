# decimal to binary conversion

def convert_to_binary(num):
    binary_array = []

    while num > 0:
        binary_array.append(num % 2)
        num = num // 2

    for i in range(len(binary_array) - 1, -1, -1):
        print(binary_array[i], end="")


# Main function
if __name__ == "__main__":
    n = 11
    convert_to_binary(n)
