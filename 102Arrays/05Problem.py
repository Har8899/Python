# counting distinct in an array part 2
def count_distinct(arr):
    count = 0

    for i in range(len(arr)):
        flag = 0
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                flag = 1
                break
        if flag == 0:
            count += 1

    return count


if __name__ == "__main__":
    arr = [5, 8, 5, 7, 8, 10]
    print(count_distinct(arr))
