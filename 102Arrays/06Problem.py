#Code for Counting Distinct Elements in an Array Part 3
def count_distinct(arr):
    arr.sort()
    count = 0
    i = 0

    while i < len(arr):
        while i < len(arr) - 1 and arr[i] == arr[i + 1]:
            i += 1
        count += 1
        i += 1

    return count


if __name__ == "__main__":
    arr = [5, 8, 5, 7, 8, 10]
    print(count_distinct(arr))
