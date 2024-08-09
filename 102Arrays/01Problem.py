# Smallest element in array
#Algorithm 1
def get_smallest(arr):
    smallest = arr[0]
    for num in arr[1:]:
        if num < smallest:
            smallest = num
    return smallest

if __name__ == "__main__":
    arr = [7, 11, 18, -3, -7, 4]
    print("The smallest element is:", get_smallest(arr))

#ALgorithm 2
def get_smallest(arr):
    arr.sort()
    return arr[0]

if __name__ == "__main__":
    arr = [7, 11, 18, -3, -7, 4]
    print("The smallest element is:", get_smallest(arr))
