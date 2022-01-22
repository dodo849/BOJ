import sys

N = int(sys.stdin.readline())
ary = list(map(int, sys.stdin.readline().split()))

dit = {}

ary2 = list(sorted(set(ary)))

for i in range(len(ary2)):
    dit[ary2[i]] = i

for i in range(N):
    print(dit[ary[i]], end = " ")
