def bfs(start):
    # 방문한 정점 체크
    global V
    visited = [0 for _ in range(V + 1)]
    queue = []
    queue.append(start)

    while(len(queue) != 0):
        v = queue.pop(0)

        if visited[v] == 0:
            print(v, end=" ")
            visited[v] = 1

        for next_v in matrix[v]:
            if visited[next_v] == 0:
                queue.append(next_v)

def dfs(v):
    if visited[v] == 1:
        return

    print(v, end=" ")
    visited[v] = 1

    for next_v in matrix[v]:
        dfs(next_v)

    return


V, E, start = map(int, input().split())
# 1차원 배열 인덱스가 정점 번호. 2차원 배열에 저장된게 연결된 정점.
matrix = [[] for _ in range(V + 1)]
# 방문한 정점 체크
visited = [0 for _ in range(V + 1)]

#정점 입력
for _ in range(E):
    v1, v2 = map(int, input().split())
    matrix[v1].append(v2)
    matrix[v2].append(v1)

#정점을 순서 정렬.
for i in range(len(matrix)):
    matrix[i].sort()


#dfs, bfs 함수호출
dfs(start)
print()
bfs(start)
print()


