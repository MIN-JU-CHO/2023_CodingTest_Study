import sys
input = sys.stdin.readline
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(x, y):
    if x==m-1 and y==n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for dx, dy in d:
        if x+dx < 0 or x+dx >=m or y+dy < 0 or y+dy >=n:
            continue
        if graph[x][y] <= graph[x+dx][y+dy]:
            continue
        dp[x][y] += dfs(x+dx, y+dy)
    return dp[x][y]

m, n = map(int, input().strip().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().strip().split())))
dp = [[-1 for _ in range(n)] for __ in range(m)]
print(dfs(0, 0))
