import sys

def test():
    n = int(sys.stdin.readline())
    arr = []
    s = []
    for _ in range(2):
        arr.append(list(map(int, sys.stdin.readline().split())))
    # print(arr)
    arr[1][1] += arr[0][0]
    arr[0][1] += arr[1][0]
    for i in range(2, n):
        arr[0][i] += max(arr[0][i-1], arr[0][i-2])
        arr[1][i] += max(arr[1][i-1], arr[1][i-2])
    print(max(arr[0][n-1], arr[1][n-1]))

T = int(sys.stdin.readline())
for _ in range(T):
    test()
