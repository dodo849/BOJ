import sys

N = int(sys.stdin.readline())

dp = [0 for _ in range(N + 1)]
dp[1] = 9
dp[2] = 17

for n in range(3, N+1):
    dp[n] = dp[n-1] * 2 - 2

print(dp[N])