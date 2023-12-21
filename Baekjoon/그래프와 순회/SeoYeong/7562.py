from collections import deque

def move_night(n, start_x, start_y, end_x, end_y):
    move = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), 
            (1, -2), (2, -1), (1, 2), (2, 1)]
    q = deque([(start_x, start_y, 0)])
    visited = set([(start_x, start_y)])

    while q:
        sx, sy, d = q.popleft()
        if sx == end_x and sy == end_y:
            print(d)
            return
        for dx, dy in move:
            nx, ny = sx + dx, sy + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny, d+1))
            


testcase = int(input())
for _ in range(testcase):
    n = int(input())
    start_x, start_y = map(int, input().split())
    end_x, end_y = tuple(map(int, input().split()))
    move_night(n, start_x, start_y, end_x, end_y)