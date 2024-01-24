import heapq

def bfs():
    q = []
    heapq.heappush(q, (0, n))
    visited = set([])
    while q:
        m, current = heapq.heappop(q)
        visited.add(current)
        if current == k: return m
        move = [current+1, current-1, current*2]
        for i, next in enumerate(move):
            if 0<=next<=100000 and next not in visited:
                if i == 2: heapq.heappush(q, (m, next))
                else: heapq.heappush(q, (m+1, next))
            
    return -1

n, k = map(int, input().split())
answer = bfs()
print(answer)