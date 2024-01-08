import sys
input = sys.stdin.readline

def dijkstra():
    import heapq 
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        start_v, end_v, w = map(int, input().split())
        graph[start_v].append([w, end_v])

    distance = [inf] * (v+1)
    hq = []
    distance[start] = 0
    heapq.heappush(hq, [0, start])

    while hq:
        current_w, current_v = heapq.heappop(hq) 
        # ignore the vertex that has bigger weight than the distance has been updated
        if distance[current_v] < current_w: continue
        # search the adjacent nodes
        for next_w, next_n in graph[current_v]:
            w = next_w + current_w
            # calculated w is smaller than the previous path value, needs to be updated
            if w < distance[next_n]:
                distance[next_n] = w
                heapq.heappush(hq, [w, next_n])

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
inf = int(1e9)
start = int(input())

dijkstra()