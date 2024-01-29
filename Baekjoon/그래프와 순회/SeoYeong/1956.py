

def floyd():
    graph = [[inf for _ in range(v)] for _ in range(v)]

    for i in range(v): graph[i][i] = 0
    for _ in range(e):
        start, end, road = map(int, input().split())
        graph[start-1][end-1] = road

    for i in range(v): # proxy
        for j in range(v):
            for k in range(v):
                graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

    # now each elements of graph[i][j] is representing the shortest path from i to j
    # so all i need to do is find the cycle, which is all possible values of graph[i][j]+graph[j][i] (i != j)
    ans = inf
    for i in range(v):
        for j in range(i+1, v):
            ans = min(ans, graph[i][j]+graph[j][i])

    if ans == inf:
        print(-1)
    else:
        print(ans)

def dijkstra():
    import heapq
    def each_optimal_of(vertex):
        hq = []
        heapq.heappush(hq, (0, vertex))
        while hq:
            sd, sv = heapq.heappop(hq)
            print(vertex, sd, sv)
            if distance[vertex][sv] <= sd: continue
            for nv, nd in graph[sv]:
                d = sd + nd
                if d < distance[vertex][nv]:
                    distance[vertex][nv] = d
                    heapq.heappush(hq, (d, nv))
        return
        
    graph = [[] for _ in range(v+1)]
    distance = [[inf for _ in range(v+1)] for _ in range(v+1)]
    for i in range(v): distance[i][i] = 0
    for _ in range(e):
        start, end, road = map(int, input().split())
        graph[start].append([end, road])
        distance[start][end] = road
    for i in range(1, v):
        each_optimal_of(i)
    print(distance)

"""
 [10000000000.0, 0, 1, 5],
 [10000000000.0, 10000000000.0, 0, 2], 
 [10000000000.0, 10000000000.0, 1, 10000000000.0]]

1->1 
2->2
3->3
"""
inf = 1e10
v, e = map(int, input().split())
floyd()