from queue import deque
n = int(input())
q = deque()
for i in range(10):
    q.append(i)
cnt = 0
while cnt <= n:
    cnt += 1
    if len(q) == 0:
        print(-1)
        exit(0)
    num = q.popleft()
    for i in range(0, num % 10):
        q.append(num * 10 + i)
print(num)
