# Bubble sort code
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range (n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def display(arr):
    print(" ".join(str(x)for x in arr))


arr = [5, 3, 1, 9, 8, 2,4, 7]

print('Before bubble sort')
print(display(arr))

bubble_sort(arr)

print('after bubble sort')
print(display(arr))

# part 2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        # for optimization when array is already sorted and no swapping happes
        swapped = False

        # sicnce, after each iteration rightmost i element are sorted
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

def display(arr):
    print(''.join(str(x) for x in arr))

arr = [10, 20, 30, 40, 50]
print('Before bubble swap sort')
print(display(arr))

bubble_sort(arr)
print('After bubble sort ')
print(display(arr))