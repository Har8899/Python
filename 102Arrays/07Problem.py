#Code for kth Smallest Element in an Array
arr = [1, 3, 2, 1, 4, 2, 5, 6, 3, 3, 4]
k = 4

# Sort the array in ascending order
arr.sort()

count = 1
for i in range(1, len(arr)):
    # Skip identical elements
    if arr[i] != arr[i - 1]:
        count += 1
        # If k-th largest element is found, print and break the loop
        if count == k:
            print(arr[i])
            break
