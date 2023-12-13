from collections import deque

def move_bfs(n, k):
    q = deque([(n, 0)])
    visited = set([])
    while q:
        current, n_move = q.popleft()
        if current == k:
            print(f"answer is {n_move}")
            return
        for next in [current*2, current+1, current-1]:
            if next <= MAX_POS and next not in visited:
                q.append((next, n_move+1))
                visited.add(next)  

MAX_POS = 100000
n, k = map(int, input().split())

move_bfs(n, k)


