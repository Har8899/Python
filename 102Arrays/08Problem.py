#Code for Finding the Frequency of elements in an Array
arr = [10, 30, 10, 20, 10, 20, 30, 10]
n = len(arr)
visited = [0] * n

for i in range(n):
    if visited[i] == 0:
        count = 1
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                count += 1
                visited[j] = 1
        print(f"{arr[i]}:{count}")
