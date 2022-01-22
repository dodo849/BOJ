import sys

N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

arrSum = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        arrSum[i][j] += int(sum(arr[:i+1][:j+1]))

print(arrSum)

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     result = 0
#
#     for row in range(x1-1, x2):
#         result += int(sum(arr[row][y1-1:y2]))
#
#     print(result)
