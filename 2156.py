import sys

'''-----입력-----'''
N = int(sys.stdin.readline())
dp = [0]
for _ in range(N):
    dp.append(int(sys.stdin.readline()))

#원본배열을 복사
dp_origin = list(dp)

'''-----풀이-----'''
#초기화
dp[2] = dp[1] + dp[2]
# dp[2] = max(dp[0]+dp_origin[1], dp_origin[1]+dp[2], dp[0], dp[2]) #dp[1]은 변경되었으므로 dp_origin 사용

#n, n-1번째 선택 시, n-3번째 dp값 사용
#n-1번 선택 X 시, n-2번째 dp값 사용
#n번째를 선택하지 않을 시 n-1번째 dp값 사용
for i in range(3, N+1):
    dp[i] = max(dp[i-2]+dp_origin[i], dp[i-3]+dp_origin[i-1]+dp_origin[i], dp[i-1])

'''-----출력-----'''
print(dp[N])