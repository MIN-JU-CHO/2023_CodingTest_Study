import sys

def input():
    return sys.stdin.readline().rstrip()

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

minimum, maximum = 0, max(lines)
result = 0

while minimum <= maximum:
    if (minimum + maximum) // 2:
      mid = (minimum + maximum) // 2 
    else:
      mid = 1 # mid가 0이 되는 경우를 방지

    total = sum([i // mid for i in lines])
    if total >= N:
      result = mid
      minimum = mid + 1
    else:
      maximum = mid - 1

print(result)
# print(maximum) # 이와 같이 해도 문제 없음