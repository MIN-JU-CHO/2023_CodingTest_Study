# 문제 풀이 링크: https://velog.io/@cuppizza/백준-1920-수-찾기-파이썬-C
# 실행 시간: 268ms 메모리: 48772 KB
# 개선 풀이
from bisect import bisect_left
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
output = list(map(int, input().split()))
for i in range(M):
    find_pos = bisect_left(arr, output[i])
    if find_pos == N or (find_pos != N and arr[find_pos] != output[i]):
        output[i] = 0
    else:
        output[i] = 1
    print(output[i])

# 기존 풀이
# 실행 시간: 452ms 메모리: 48780 KB
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
