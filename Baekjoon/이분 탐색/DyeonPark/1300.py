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

# K보다 작거나 같은 최대값 구하기 (이분탐새 이용)
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
