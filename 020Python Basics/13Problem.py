# Break Statement

# Python (For Loop)
low, high = input("Enter the two numbers: ").split()

for i in range(int(low), int(high)+1):
    print(i, end = " ")
    if i % 13 == 0:
        break
# Python (While Loop)
list1 = list(map(int, input("Numbers: ").split()))
# list1 = [int(x) for x in input("Numbers: ").split()]
# list1 = [int(x) for x in input("Numbers: ").split(',')]

low = list1[0]
high = list1[1]

while low <= high:
    print(low, end=" ")
    if int(low) % 13 == 0:
        break
    low += 1