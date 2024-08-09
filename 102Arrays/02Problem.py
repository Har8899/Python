# second smallest array
def sec_smallest(arr):
    arr.sort()
    return arr[1]

if __name__ == "__main__":
    arr = [7, 11, 18, -3, -7, 4]
    print("The 2nd smallest element is:", sec_smallest(arr))
