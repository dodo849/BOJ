A, B, C = map(int, input().split())

if B % 2 == 0:
    print(A^2 % C)
else:
    print(A^3 % C)
