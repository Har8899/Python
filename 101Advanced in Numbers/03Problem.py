# HCF OR GCD


# Function to find HCF (GCD) of two numbers
def hcf(num1, num2):
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# Main function
if __name__ == "__main__":
    num1, num2 = 36, 72
    hcf_result = hcf(num1, num2)
    print(f"The HCF of two numbers is: {hcf_result}")

