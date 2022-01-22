import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global cnt

    for px, py in near:
        nx = x + px
        ny = y + py
        if nx >= 0 and nx < N and ny >= 0 and ny < M: #범위
            if grid[ny][nx] == 0:
                grid[ny][nx] = 1 #탐색한 영역은 1로 바꾼다
                cnt += 1
                dfs(nx, ny)
    return

#입력
M, N, K = map(int, sys.stdin.readline().split())

grid = [[0 for _ in range(N)] for _ in range(M)]

#직사각형 영역이 있는 부분을 1로 변경
for _ in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())

    for i in range(lx, rx):
        for j in range(ly, ry):
            grid[j][i] = 1

#상하좌우 값
near = [[0, -1], [0, 1], [-1, 0], [1, 0]]

#영역 크기 저장
area = []

#모든 좌표에 대해 dfs가능한지 확인하고 dfs
for i in range(N):
    for j in range(M):
        #직사각형 영역이 아니거나, 아직 탐색하지 않은 영역만 dfs
        if grid[j][i] == 0:
            cnt = 1
            grid[j][i] = 1
            dfs(i, j)
            area.append(cnt)

#출력
area.sort()
print(len(area))
for a in area:
    print(a, end=" ")
