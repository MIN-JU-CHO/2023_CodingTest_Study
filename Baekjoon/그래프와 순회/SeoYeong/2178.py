
def bfs():
    from collections import deque
    queue = deque([(0, 0, 1)])
    while queue:
        sx, sy, mv = queue.popleft()
        if sx == n-1 and sy == m-1:
            print(mv)
            return
        for dx, dy in move:
            nx, ny = sx + dx, sy + dy
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = -1
                queue.append((nx, ny, mv+1))



n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

bfs()

