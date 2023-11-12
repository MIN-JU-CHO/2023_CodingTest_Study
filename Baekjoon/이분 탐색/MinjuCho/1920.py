from bisect import bisect_left

def binary_search(key):
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start + end) // 2
        if arr[mid] == key:
            return 1
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1
    return 0

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
output = list(map(int, input().split()))
for i in range(M):
    output[i] = binary_search(output[i])
    print(output[i], end = ' ')
