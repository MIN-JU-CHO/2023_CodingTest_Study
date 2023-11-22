n = int(input())
e = int(input())

visited = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(e):
    e1, e2 = map(int, input().split())
    graph[e1].append(e2)
    graph[e2].append(e1)

visited[1] = 1
stack = graph[1]

while stack:
    top = stack.pop()
    visited[top] = 1
    for v in graph[top]:
        if not visited[v]: # visited[v]=0 일때
            stack.append(v)
        
print(sum(visited)-1)


