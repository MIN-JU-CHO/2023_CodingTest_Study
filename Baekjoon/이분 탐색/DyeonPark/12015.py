import sys

def input():
  return sys.stdin.readline().rstrip()

def parametric_search(arr, target):
  start, end = 0, len(arr) - 1
  max_pos = 0

  while start <= end:
    mid = (start + end) // 2
    if arr[mid] >= target:
      end = mid - 1
      max_pos = mid
    else:
      start = mid + 1
      
  return max_pos

N = int(input())
nums = list(map(int, input().split()))

res = [nums[0]]
for i in range(1, N):
  if nums[i] >= res[-1]: # 추가되는 원소가 LIS 배열의 최대값보다 크거나 같을 때
    res.append(nums[i])
  else: # 선행 원소보다 작을 때
    idx = parametric_search(res, nums[i]) # 추가되는 원소가 LIS 배열의 최대값보다 작을때 -> 대치되어 들어갈 수 있는 위치 찾기(파라메트릭탐색)
    res[idx] = nums[i] # 값 대치
    # print(nums[i], "보다 크지만 가장 작은 수는 res의", idx, "에 위치한", res[idx])

# print(res)
print(len(res))