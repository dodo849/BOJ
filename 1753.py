import heapq
import sys

def dijkstra(start):
    global INF

    heap = [] # 한 정점으로 갈 때의 최단경로를 추가.
    distance = [INF for _ in range(V+1)]

    # 1. 시작 정점을 힙에 추가. 자기자신이므로 가중치는 0 : (도착정점, 가중치)
    heapq.heappush(heap, (0, start))

    # 힙이 빌 때 까지 반복
    while heap:
        # 2. 현재 존재하는 경로 중에서 최단 경로인 정점(v)과 가중치(w)를 pop
        w, v = heapq.heappop(heap)

        # 이 조건은 사실 이해가 안된다.
        if distance[v] < w:
            continue

        # 3. v를 거쳐서 to_v로 가는 경로 중 최단 경로가 있는지 확인
        for to_v, to_w in graph[v]: # v에 연결된 간선을 탐색한다.
            # 4. v를 거쳐 to_v로 가는 비용이 지금까지 확인된 경로보다 최단 거리라면 교체한다.
            # 그리고 교체된 경로를 heap에 추가한다.
            cost = to_w + w
            if cost < distance[to_v]:
                distance[to_v] = cost
                heapq.heappush(heap, (cost, to_v))
    return distance

# 입력
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
INF = 100000000000 #무한대를 큰 수로 임의로 지정
graph = [ [] for _ in range(V+1)] #정점 개수+1만큼 생성

# 방향그래프 저장 인덱스:시작정점, (도착정점, 가중치)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# i+1번 정점으로 가는 최단경로를 저장한 배열 distance를 반환
distance = dijkstra(K)
# 자기 자신으로 가는 경로는 0으로
distance[K] = 0

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])