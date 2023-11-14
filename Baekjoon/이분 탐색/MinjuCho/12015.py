# 문제 풀이 링크: https://velog.io/@cuppizza/백준-12015-가장-긴-증가하는-부분-수열-2-C-파이썬
# 실행 시간: 1008ms 메모리: 145332KB
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
