from collections import deque

def pprint():
    for g in graph:
        print(g, end='\n')
    print()

def bfs():
    if n == m == 1: 
        return 1

    def cardinal_search(next_search_amt: int, break_flag: bool, loop_flag: bool):
        direction = [(x*next_search_amt, y*next_search_amt) for x, y in cardinal]
        for dx, dy in direction:
            nx, ny = sx + dx, sy + dy
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in visited and graph[nx][ny]==0:
                visited.add((nx, ny))#; pprint()
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

        # 현재 누락된 케이스 ) 갈 수 있는 경로가 존재하긴 하지만 벽을 뚫으면 최단경로로 이동할 수 있을때 (갈 수 없을 때만 벽 뚫는거 고려함)
        if break_flag:
            if loop_flag:
                cardinal_search(2, break_flag, loop_flag)
            if (sx == n-3 and sy == m-1 and graph[n-2][m-1] == 1) or \
            (sx == n-1 and sy == m-3 and graph[n-1][m-2] == 1):
                return move+2

    return -1

# while True:
n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]

cardinal = [(0, 1), (1, 0), (0, -1), (-1, 0)]
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