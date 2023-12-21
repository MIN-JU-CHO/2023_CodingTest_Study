from queue import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
graph = [[0 for __ in range(m)] for _ in range(n)]
for i in range(n):
    row = input().strip()
    for j in range(m):
        if row[j] == '1':
            graph[i][j] = 1
# BFS
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque([(0, 0)])
graph[0][0] = 2
while q:
    x, y = q.popleft()
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] != 1: # wall or visited
            continue
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))
print(graph[n-1][m-1] - 1)
