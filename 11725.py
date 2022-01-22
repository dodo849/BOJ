import sys

def bfs():
    queue = [1]
    while len(queue) != 0:
        this = queue.pop(0)
        for i in range(len(tree[this])):
            if visited[tree[this][i]] != 1:
                result[tree[this][i]] = this
                queue.append(tree[this][i])
        visited[this] = 1

n = int(sys.stdin.readline())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

result = [0 for _ in range(n+1)] #각 인덱스=노드번호 의 부모를 저장
visited = [0 for _ in range(n+1)]
bfs()

for i in range(2, n+1):
    if tree[i] != []:
        print(result[i])