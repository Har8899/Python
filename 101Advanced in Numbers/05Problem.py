# lcm part 2
# Function to get LCM of two numbers
def get_lcm(num1, num2):
    max_num = max(num1, num2)
    while True:
        if max_num % num1 == 0 and max_num % num2 == 0:
            return max_num
        max_num += 1

# Main function
if __name__ == "__main__":
    num1, num2 = 36, 60
    lcm_result = get_lcm(num1, num2)
    print(f"The LCM of two numbers is: {lcm_result}")
