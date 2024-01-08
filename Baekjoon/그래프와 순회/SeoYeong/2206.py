from collections import deque

def pprint():
    for g in graph:
        print(g, end='\n')
    print()

def bfs():
    def cardinal_search(next_search_amt: int, break_flag: bool, loop_flag: bool):
        direction = [(x*next_search_amt, y*next_search_amt) for x, y in cardinal]
        for dx, dy in direction:
            nx, ny = sx + dx, sy + dy
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and graph[nx][ny]==0:
                visited.add((nx, ny)) ; pprint()
                graph[nx][ny] = -2
                if next_search_amt == 1: 
                    q.append((nx, ny, move+1, break_flag))
                    loop_flag = False
                else:
                    q.append((nx, ny, move+1, False))
        return loop_flag
    
    while q:
        sx, sy, move, break_flag = q.popleft()
        if sx == n-1 and sy ==m-1: 
            return move+1

        loop_flag = True # 4방향 탐색 다 막혀있는지?
        loop_flag = cardinal_search(1, break_flag, loop_flag)

        if loop_flag and break_flag:
            cardinal_search(2, break_flag, loop_flag)

    return -1

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

cardinal = [(-1, 0), (0, 1), (1, 0), (0, -1)]
break_flag = True # 벽 부실 기회 있는지?
visited = set([(0, 0)])
q = deque([(0, 0, 1, True)])

ans = bfs()
print(ans)


'''
6 4
0100
1110
1000
0000
0111
0000
'''