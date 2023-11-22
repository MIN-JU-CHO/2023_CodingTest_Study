def dfs(graph: list, v: int, visited: list):
    visited.add(v)
    print(v, end=" ")

    for adj in graph[v]:
        if adj not in visited:
            dfs(graph, adj, visited)

def bfs(graph: list, v: int):
    from collections import deque

    visited = set()

    q = deque([v])
    while q:
        v = q.popleft()
        if v not in visited:
            visited.add(v)
            print(v, end=" ")
            q.extend(graph[v]-visited)
        



n, m, v = map(int, input().split()) # 정점 개수, 간선 개수, 탐색 시작 정점 번호
graph = [set() for _ in range(n+1)]
for _ in range(m):
    e1, e2 = map(int, input().split())
    graph[e1].add(e2)
    graph[e2].add(e1)

dfs(graph, v, set([]))
print()
bfs(graph, v)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
    1 2 4 3
    1 2 3 4
5 5 3
5 4
5 2
1 2
3 4
3 1
    3 1 2 5 4
    3 1 4 2 5
1000 1 1000
999 1000
    1000 999
    1000 999
"""