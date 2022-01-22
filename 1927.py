import sys

n = int(sys.stdin.readline())

array = []

for _ in range(n):
    temp = int(sys.stdin.readline())
    if temp == 0:
        if len(array) == 0:
            print(0)
        else:
            print(min(array))
            array.remove(min(array))
    elif temp > 0:
        array.append(temp)