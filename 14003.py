import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

d = [0 for _ in range(N)]
d[0] = 1


for i in range(1, N):
    if arr[i-1] < arr[i] and d[i-2] < d[i-1] + 1:
        d[i] += d[i-1] + 1
    else:
        d[i] = d[i-1]

print(max(d))


