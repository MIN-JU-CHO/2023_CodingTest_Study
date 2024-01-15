import sys
input = sys.stdin.readline
n = int(input())
time, profit = [], []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    profit.append(p)

dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1):
    if i + time[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], profit[i] + dp[i+time[i]])
    print(dp)



print(f"answer is {max(dp)}")