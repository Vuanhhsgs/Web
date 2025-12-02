t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_dp = [[0] * n for j in range(2)]
    max_dp = [[0] * n for j in range(2)]
    min_dp[0][0] = a[0]
    max_dp[0][0] = a[0]
    min_dp[1][0] = b[n-1]
    max_dp[1][0] = b[n-1]
    for i in range(0,n-1):
        min_dp[0][i+1] = min(min_dp[0][i], a[i+1])
        max_dp[0][i+1] = max(max_dp[0][i], a[i+1])
        min_dp[1][i+1] = min(min_dp[1][i], b[n-i-2])
        max_dp[1][i+1] = max(max_dp[1][i], b[n-i-2])
    def pair_of_lr_satisfy(minimum, maximum):
        return minimum * (2*n+1-maximum)
    intersect_dp = [[0] * n for j in range(n)]
    def intersect(a, b):
        m = max(a,b)
        p = min(a,b)
        return pair_of_lr_satisfy( min(min_dp[0][m-1], min_dp[1][n-p]), max(max_dp[0][m-1], max_dp[1][n-p])  )
    def go_down_at_column(m):
        return pair_of_lr_satisfy( min(min_dp[0][m-1], min_dp[1][n-m]) , max(max_dp[0][m-1], max_dp[1][n-m]) )
    def func(m):
        if m == 1:
            return pair_of_lr_satisfy( min(min_dp[0][0], min_dp[1][n-1]), max(max_dp[0][1], max_dp[1][n-1]) ) 
        else:
            return func(m-1) + go_down_at_column(m) - intersect(m-1, m)
    print(func(n))