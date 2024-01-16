import heapq

def dijkstra(start: int):
    """
    make optimal distance list of given vertex `start` 
    """
    distance[start][start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        cw, cv = heapq.heappop(hq)
        if distance[start][cv] < cw: continue
        for nw, nv in graph[cv]:
            w = cw + nw
            if distance[start][nv] > w:
                distance[start][nv] = w
                heapq.heappush(hq, (w, nv))
    return


v, e = map(int, input().split())
inf = 1e10
graph = [[] for _ in range(v+1)]
for _ in range(e):
    x, y, w = map(int, input().split())
    graph[x].append((w, y))
    graph[y].append((w, x))

p1, p2 = map(int, input().split()) # 경유 정점

distance = {p1:[inf for _ in range(v+1)],
            p2:[inf for _ in range(v+1)]}

dijkstra(p1)
dijkstra(p2)

# 1-> p1 -> p2 -> n : distance[p1][1] + distance[p1][p2] + distance[p1][v]
# 1-> p2 -> p1 -> n : distance[p2][1] + distance[p1][p2] + distance[p2][v]
start_p1 = distance[p1][1]; start_p2 = distance[p2][1]
p1_p2 = distance[p1][p2]
p2_end = distance[p2][v]; p1_end = distance[p1][v]

path1 = [start_p1, p1_p2, p2_end]
path2 = [start_p2, p1_p2, p1_end]

if inf in path1 and inf in path2:
    print(-1)
else:
    print(min(sum(path1), sum(path2)))
