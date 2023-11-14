# 문제 풀이 링크: https://velog.io/@cuppizza/백준-2805-나무-자르기-C-파이썬
# 실행 시간: 4636ms 메모리: 143264KB
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
