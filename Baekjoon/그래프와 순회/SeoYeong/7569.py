from collections import deque
m, n, h = map(int, input().split()) # 가로, 세로, 높이

warehouse = []
numof_unriped = 0
ripe_info = []

for i in range(h):
    tmp = []
    for j in range(n):
        # 한 상자에 담긴 토마토 정보
        row = list(map(int, input().split()))
        tmp.append(row)
        for k in [k for k, r in enumerate(row) if r == 1]:
            ripe_info.append((i, j, k, 0))
        numof_unriped += len([r for r in row if r == 0])
    warehouse.append(tmp)

ripe = deque(ripe_info)
visited = set(ripe_info)
# for w in warehouse: print(w)
# print(ripe, numof_unriped, visited)

move = ((1, 0, 0), (-1, 0, 0), 
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1))
print(h, n, m)
while ripe:
    sh, sx, sy, day = ripe.popleft()
    for dh, dx, dy in move:
        nh, nx, ny = sh+dh, sx+dx, sy+dy
        if 0<=nh<h and 0<=nx<n and 0<=ny<m and (nh, nx, ny) not in visited and warehouse[nh][nx][ny] == 0:
            ripe.append((nh, nx, ny, day+1))
            visited.add((nh, nx, ny))
            warehouse[nh][nx][ny] = 1
            numof_unriped -= 1

if numof_unriped == 0:
    print(day)
else:
    print(-1)


