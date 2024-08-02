# Greatest of Two No.

# Method 1
first = int(input("Enter first number:"))
second = int(input("Enter second number:"))

if first == second:
    print("Both are Equal")
elif first > second:
    print(str(first) + " is Greater")
else:
    print(str(second) + " is Greater")

# Method 2

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))

if first == second:
    print("Both are Equal")
else:
    result = first if first > second else second
    print(str(result) + " is greater")

# Method 3

first = int(input("Enter first number:"))
second = int(input("Enter second number:"))

if first == second:
    print("Both are Equal")
else:
    result = max(first, second)
    print(str(result) + " is greater")