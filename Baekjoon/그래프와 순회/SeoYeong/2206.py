from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
further_direction = [(-2, 0), (0, 2), (2, 0), (0, -2)]
break_flag = True # 벽 부실 기회 있는지?

visited = set([(0, 0)])
q = deque([(0, 0, 1, True)])

while q:
    sx, sy, move, break_flag = q.popleft()
    if sx == n-1 and sy ==m-1: 
        break

    loop_flag = True # 4방향 탐색 다 막혀있는지?
    for dx, dy in direction:
        nx, ny = sx + dx, sy + dy
        if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and graph[nx][ny]==0:
            visited.add((nx, ny))
            q.append((nx, ny, move+1, break_flag))
            loop_flag = False

    if loop_flag and break_flag:
        for dx, dy in further_direction:
            nx, ny = sx + dx, sy + dy
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and graph[nx][ny]==0:
                visited.add((nx, ny))
                q.append((nx, ny, move+1, False))


print(move+1)
'''
6 4
0100
1110
1000
0000
0111
0000
'''