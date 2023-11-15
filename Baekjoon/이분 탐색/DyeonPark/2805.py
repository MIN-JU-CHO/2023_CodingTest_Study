import sys

def input():
  return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)
answer = 0
while start <= end:
  mid = (start + end) // 2
  
  cut_sum = sum([t - mid for t in trees if t > mid])
  # cut_sum = sum([max(t - mid, 0) for t in trees]) # 시간 초과 - Pypy로는 가능

  if cut_sum >= M:
    start = mid + 1
    answer = mid
  else:
    end = mid - 1

print(answer)