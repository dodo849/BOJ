import sys

'''-----입력-----'''
F, S, G, U, D = map(int, sys.stdin.readline().split())

'''-----풀이-----'''
arr = [-1 for _ in range(F+1)]

q = [S]
arr[S] = 0

flag = 0 #1이면 값 찾음. 2면 못찾음.
while q:
    S = q.pop(0)

    if S == G:
        flag = 1
        print(arr[G])
        break

    if S+U <= F and arr[S+U] == -1:
        arr[S+U] = arr[S] + 1
        q.append(S+U)
    if S-D > 0 and arr[S-D] == -1:
        arr[S-D] = arr[S] + 1
        q.append(S-D)

if flag == 0:
    print("use the stairs")

