import sys
from math import *

# MAX = 230
MAX = 107
N = int(sys.stdin.readline())

Squares = []

for i in range(1, MAX):
    Squares.append(i*i)

cnt = 0
max = MAX-2
while(N>0):
    for i in range(max, -1, -1):
        temp = N - Squares[i]

        if temp >= 0:
            N = N - Squares[i]
            print(temp, '템프')
            print(Squares[i], i , '제곱')
            max = i
            break
    cnt += 1
print(cnt)