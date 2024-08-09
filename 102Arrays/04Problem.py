# counting distinct in an array part 1
def count_unique_elements(arr):
    visited = [False] * len(arr)
    count_dis = 0

    for i in range(len(arr)):
        if not visited[i]:
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    visited[j] = True
            count_dis += 1

    return count_dis


if __name__ == "__main__":
    arr = [30, 50, 30, 10, 20, 40, 10, 20]
    print(count_unique_elements(arr))
