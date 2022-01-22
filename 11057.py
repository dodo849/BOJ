import sys

'''-----입력-----'''
N = int(sys.stdin.readline())

'''-----풀이-----'''
dp = [[1 for _ in range(10)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, 10):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

'''-----출력-----'''

print(dp[N][9] % 10007)