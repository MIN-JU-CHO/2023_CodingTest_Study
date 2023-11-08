N = int(input())
K = int(input())
start = 1
end = K
while start<=end:
    mid = (start+end)//2
    count = 0
    # 탐색 값 // 행 값: 탐색 값보다 작은 배수의 개수
    for i in range(1, N+1):
        count += min(mid // i, N)
    if count < K:
        start = mid+1
    else:
        result = mid
        end = mid-1
print(result)
