from queue import deque
n, k = map(int, input().split())
position = [-1 for _ in range(100001)]
position[n] = 0
q = deque()
q.append(n)
while q:
    cur = q.popleft()
    if cur - 1 >= 0 and position[cur-1] == -1:
        position[cur-1] = position[cur] + 1
        q.append(cur-1)
    if cur + 1 < 100001 and position[cur+1] == -1:
        position[cur+1] = position[cur] + 1
        q.append(cur+1)
    if cur * 2 < 100001 and position[cur*2] == -1:
        position[cur*2] = position[cur] + 1
        q.append(cur*2)
    if cur - 1 == k or cur + 1 == k or cur * 2 == k:
        print(position[k])
        exit(0)