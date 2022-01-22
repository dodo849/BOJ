import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

memo = [0 for _ in range(N)]
cnt = 0
def dynamic():
    for i in range(0, N):
        for j in range(0, i):
            if(arr[i] > arr[j] and memo[i] <= memo[j]):
                memo[i] = memo[j]
        memo[i] += 1
dynamic()
print(max(memo))