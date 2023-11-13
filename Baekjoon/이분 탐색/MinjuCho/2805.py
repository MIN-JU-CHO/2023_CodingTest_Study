import sys
input = sys.stdin.readline
N, M = map(int, input().split())
woods = list(map(int, input().split()))

start = 1
end = max(woods)
result = 0
while start<=end:
    mid = (start + end) // 2
    count = 0
    for timber in woods:
        if timber>mid:
            count += timber - mid
    if count >= M:
        result = max(mid, result)
        start = mid+1
    else:
        end = mid-1
print(result)
