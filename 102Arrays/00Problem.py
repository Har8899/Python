# Linear Search
def linear_search(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            print(f"{item} Found at index: {i}")
            return
    print("Not found")

if __name__ == "__main__":
    arr = [10, 5, 15, 21, -3, 7]
    item = 21
    linear_search(arr, item)
