from collections import deque

# 인접한 애들 모두 탐색(너비 탐색)
m, n = map(int, input().split())
warehouse = []
ripe = deque([])
for i in range(n):
    l = list(map(int, input().split()))
    for j in [j for j, val in enumerate(l) if val == 1]:
        ripe.append((i, j, 0))
    warehouse.append(l)

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while ripe:
    sx, sy, day  = ripe.popleft()
    warehouse[sx][sy] = -1
    for dx, dy in move:
        nx, ny = sx + dx, sy + dy
        if 0<=nx<n and 0<=ny<m and warehouse[nx][ny] == 0:
            ripe.append((nx, ny, day+1))

if sum(sum(warehouse, [])) == m*n:
    print(day)
else:
    print(-1)