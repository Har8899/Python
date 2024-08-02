# Continue Statement

low, high = input("Enter the two numbers: ").split()

for i in range(int(low), int(high)+1):
    if i % 5 == 0:
        continue
    print(i, end=" ")

