import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input().strip())
m = int(input().strip())
adj = [[INF for _ in range(n+1)] for __ in range(n+1)]
while m:
    m-=1
    a, b, c = map(int, input().strip().split())
    if c < adj[a][b]:
        adj[a][b] = c
for i in range(1, n+1):
    adj[i][i] = 0
for i in range(1, n+1):
    for s in range(1, n+1):
        for t in range(1, n+1):
            if adj[s][i] + adj[i][t] < adj[s][t]:
                adj[s][t] = adj[s][i] + adj[i][t]
for s in range(1, n+1):
    for t in range(1, n+1):
        if adj[s][t] == INF:
            print("0", end =' ')
            continue
        print(adj[s][t], end = ' ')
    print()
