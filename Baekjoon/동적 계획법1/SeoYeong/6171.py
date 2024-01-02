def clone_coded():
    n = int(input())
    lands = [list(map(int, input().split())) for _ in range(n)] # [w, h]

    def compare(w, h):
        return (-w, h)
    
    lands.sort(key=compare)

    land = lands[0]
    for i in range(1, n):
        next = lands[i]
        now = land[-1]
        if next[1] > now[1]: 
            land.append(next)

    def _dp(land):
        dp = [0]*len(land)
        for i in range(1, len(land)):
            dp[i] = dp[i-1] + land[i][0] * land[i][1]
            for j in range(i, 0, -1):
                dp[i] = min(dp[i], dp[j-1] + land[j][0]*land[j][1])
        return dp[-1]
    
    answer = _dp(land)
    
    