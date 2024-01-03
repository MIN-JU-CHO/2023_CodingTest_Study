def dijkstra():
    graph = {}
    for _ in range(e):
        start_v, end_v, w = map(int, input().split())
        graph[(start_v, end_v)] = w

    spt = [False] * (v+1)
    distance = [inf] * (v+1)
    distance[start] = 0

    def min_distance():
        min = inf
        for u in range(1, v+1):
            if distance[u] < min and spt[u] == False:
                min = distance[u]
                min_idx = u
        return min_idx
    
    for _ in range(1, v+1):
        x = min_distance()
        spt[x] = True
        for y in range(1, v+1):
            if (x, y) in graph.keys() and spt[y] == False:
                distance[y] = min(distance[y], distance[x]+graph[(x, y)])
        print(x, spt, distance)

    for i in range(1, v+1):
        if distance[i] == inf: print('INF')
        else: print(distance[i])


def initial_approach():
    from collections import defaultdict   
    graph = defaultdict(list)
    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[e].append((s, w))

    start_to_idx = [0 for _ in range(v+1)]
    
    for i in range(1, v+1):
        if i == start: continue
        optimal_path = inf
        for j, weight in graph[i]:
            if i == j: continue
            optimal_path = min(optimal_path, weight + start_to_idx[j])
        start_to_idx[i] = optimal_path

    for i in range(1, v+1):
        if i != start and start_to_idx[i] == 0: print('INF')
        else: print(start_to_idx[i])


v, e = map(int, input().split())
inf = 11*(v-1)+1 # w 최댓값 10, 경로가 모든 노드를 거쳐서 오는 최대 경로 케이스를 고려하면 최댓값은 11*(v-1)
start = int(input())

dijkstra()