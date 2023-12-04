from collections import deque

def _print(graph):
    for g in graph: print(g)
    print()

def is_in_range(x: int, y: int) -> bool:
    global n, m
    if x>=0 and x<n and y>=0 and y<m:
        return True
    return False

# visited : graph에 -1 표시
def search_land(graph: list, lettace: list, x: int, y: int) -> list:
    q = deque([(x, y)])
    four_direction = [[-1, 0, 1, 0],
                      [0, -1, 0, 1]]
    while q:
        nx, ny = q.popleft()
        graph[nx][ny] = -1
        for i in range(4):
            sx, sy = nx + four_direction[0][i], ny + four_direction[1][i]
            if is_in_range(sx, sy) and graph[sx][sy] == 1:
                q.append((sx, sy))
    return graph


test_case = int(input())
for _ in range(test_case):
    m, n, k = map(int, input().split())
    print(m, n, k)
    graph = [[0 for _ in range(m)] for _ in range(n)]

    lettace_location = []
    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
        lettace_location.append((x, y))
    
    insect = 0

    if sum(sum(graph, [])) in [0, 1]:
        print(str(sum(sum(graph, []))))
        pass

    for (i, j) in lettace_location:
        if graph[i][j] == 1:
            graph, lettace_location = search_land(graph, lettace_location, i, j)
            insect += 1
            # _print(graph)

    # _print(graph)
    print(insect)
