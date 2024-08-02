# Implementing 1D array


#Python (Method 1)
num = int(input("Enter the Size of Array :"))
arr = []

print("The elements are : ")
for i in range(num):
    arr.append(int(input()))

print("The elements are : ")

for i in range(num):
    print(arr[i], end=" ")

# alternate way you can print but in list format
# print(arr)


##Python (Method 2)
num = int(input("Enter the Size of Array :"))
arr = [int(x) for x in input("Enter the Elements : ").split()]


print("The elements are : ")

# for i in range(num):
#     print(arr[i], end=" ")

# alternate way you can print but in list format
print(arr)


#Python (Method 3)
num = int(input("Enter the Size of Array :"))
arr = []

print("Enter the numbers")
while num > 0:
    arr.append(int(input()))
    num -= 1

print("The elements are : ")

for item in arr:
    print(item, end=" ")

# alternate way you can print but in list format
# print(arr)
