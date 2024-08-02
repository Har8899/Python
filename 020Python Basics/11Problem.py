# Greatest of Three No.

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))
third = int(input("Enter third number:"))

if first > second and first > third:
    print(str(first) + " is greatest")
elif second > first and second > third:
    print(str(second) + " is greatest")
else:
    print(str(third) + " is greatest")

# Method 2

temp = first if first > second else second

result = temp if temp > third else third
print(str(result) + " is the greatest")

# Method 3

result = max(first, max(second, third))
print(str(result) + " is greatest")
