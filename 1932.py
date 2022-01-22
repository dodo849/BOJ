import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
print(arr)

arr[1][0] += arr[0][0]
arr[1][1] += arr[0][0]

for i in range(2, N):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][0]
        elif j == i:
            arr[i][j] += arr[i-1][j-1]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])
print(max(arr[N-1]))