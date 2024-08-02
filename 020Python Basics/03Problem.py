# Positive or Negative NO.

# Method 1
num = int(input("Insert a number:"))
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("Zero")


# Method 2

num = int(input("Insert a number:"))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")

# Method 3

num = int(input("Insert a number:"))
if num == 0:
    print("Zero")
else:
    result = "Positive" if num > 0 else "Negative"
    print(result)

