from bisect import bisect_left
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = []
for elem in A:
    index = bisect_left(dp, elem)
    if index == len(dp):
        dp.append(elem)
    else:
        dp[index] = elem
print(len(dp))
