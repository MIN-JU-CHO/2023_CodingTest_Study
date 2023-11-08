import sys
input = sys.stdin.readline
K, N = map(int,input().split())
array = [0] * K
for i in range(K):
    array[i]=int(input())
max_length = 0
start = 1
end = max(array)
# 크롭 길이 범위 내에서 찾기
while start <= end:
    mid = (start+end)//2
    n=0
    # 크롭 개수 update
    for cable in array:
        n += cable//mid
    # 길게 잘랐을 때
    if n<N:
        end = mid-1
    # 더 길게 자를 수 있을 때
    else:
        max_length = mid
        start = mid+1
print(max_length)
