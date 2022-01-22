import sys
sys.setrecursionlimit(100000)

def sum(n):
    dynamic = [1, 2, 4]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return sum(n-1) + sum(n-2) + sum(n-3)

T = int(sys.stdin.readline())
result = []
for _ in range(T):
    n = int(sys.stdin.readline())
    result.append(sum(n))
for r in result:
    print(r)