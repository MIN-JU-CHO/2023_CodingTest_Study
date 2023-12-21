from collections import deque

# 인접한 애들 모두 탐색(너비 탐색)
m, n = map(int, input().split())
warehouse = []
ripe = deque([])
numof_unripe = 0
for i in range(n):
    l = list(map(int, input().split()))
    for j in [j for j, val in enumerate(l) if val == 1]:
        ripe.append((i, j, 0))
    numof_unripe += len([val for val in l if val == 0])
    warehouse.append(l)

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = set([]) # 초기 노드 넣어주기
while ripe:
    sx, sy, day  = ripe.popleft()
    for dx, dy in move:
        nx, ny = sx + dx, sy + dy
        if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and warehouse[nx][ny] == 0:
            ripe.append((nx, ny, day+1))
            visited.add((nx, ny))
            warehouse[nx][ny] = 1
            numof_unripe -= 1

for i in warehouse:
    print(i)

if numof_unripe == 0:
    print(day)
else:
    print(-1)