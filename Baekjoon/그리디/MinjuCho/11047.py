import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input().strip()))
result = 0
for i in range(n-1, -1, -1):
    result += k // coins[i]
    k %= coins[i]
print(result)
