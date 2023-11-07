# 정답 풀이
# 참고1: https://velog.io/@uoayop/BOJ-1300-K%EB%B2%88%EC%A7%B8-%EC%88%98Python
# 참고2: https://claude-u.tistory.com/449
import sys

def input():
  return sys.stdin.readline().rstrip()

N, K = int(input()), int(input())

# K번째 수는 K보다 클 수 없음!
# 따라서 K보다 작은 수에 대해 곱이 몇 개인지 찾아내면 됨
start, end = 1, K
result = 0

while start <= end:
  mid = (start + end) // 2

  # mid를 만들기 위해 주어진 수 에서 몇 개의 조합으로 만들 수 있는지 카운팅
  cnt = 0
  for i in range(1, N + 1):    
    cnt += min(mid // i, N)

  if cnt >= K: # 목표(K)보다 많거나 같은 경우 (최대화를 위함)
    result = mid
    end = mid - 1
  else: # 목표(K)보다 적은 경우
    start = mid + 1

print(result)


##################################### 
############## 틀린 풀이 ############## 
##################################### 

import sys
from itertools import accumulate

def input():
  return sys.stdin.readline().rstrip()

N = int(input())
K = int(input())

# 대각선 별 값 개수 구하기
nums = [i for i in range(1, N)]
for i in range(N, 0, -1):
  nums.append(i)

# 대각선 별 값 개수 누적값 구하기
acc_nums = [i for i in accumulate(nums)]

# K보다 작거나 같은 최대값 구하기 (이분탐색 이용)
start = 0
end = len(acc_nums) - 1
result = 0
while start <= end:
  mid = (start + end) // 2
  if acc_nums[mid] >= K:
    end = mid - 1
    result = mid
  else:
    start = mid + 1

fin_idx = K - acc_nums[result] - 1

N_list = list(range(1, N + 1))
if result <= len(acc_nums) // 2:
  ij_list = N_list[result::-1]
else:
  ij_list = N_list[-1:result % N:-1]

diag = []
for i, j in zip(ij_list, ij_list[::-1]):
  diag.append(i * j)

diag.sort()
term = K - acc_nums[result]
print(diag[term])
