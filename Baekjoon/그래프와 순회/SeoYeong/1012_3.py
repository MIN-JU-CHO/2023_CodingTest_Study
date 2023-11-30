
def dfs(x: int, y: int):
    four_direction = [[-1, 0, 1, 0],
                      [0, -1, 0, 1]]
    for i in range(4):
        nx, ny = x + four_direction[0][i], y + four_direction[1][i]
        if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)
    return -1

# dfs with stack
def dfs_stack(x, y):
    four_direction = [[-1, 0, 1, 0],
                      [0, -1, 0, 1]]
    stack = [(x, y)]
    while stack:
        (sx, sy) = stack.pop()
        for i in range(4):
            nx, ny = sx + four_direction[0][i], sy + four_direction[1][i]
            if (0 <= nx < n) and (0 <= ny < m) and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append((nx, ny))

test_case = int(input())
for _ in range(test_case):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1

    insect = 0
    if sum(sum(graph, [])) in [0, 1]:
        print(str(sum(sum(graph, []))))
        pass

    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                dfs_stack(x, y)
                insect += 1

    print(insect)