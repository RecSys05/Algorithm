'''
N:도시 개수(노드), M:도로 개수(선), K:거리 정보(조건), X:출발 도시 번호(시작, index+1)
A번 도시 - B번 도시
'''
import sys
import heapq

input = sys.stdin.readlines
user_input = input()
N, M, K, X = list(map(int,user_input[0].split()))
arrs = [list(map(int, i.split())) for i in user_input[1:]]

# 노드 그래프 만들기
graph = [[] for _ in range(N)]
for start_node, end_node in arrs:
    graph[start_node-1].append(end_node-1)

# 방문 리스트 만들기 
visited = [False] * N

# 거리 리스트 만들기
distances = [float("inf")] * N

# sort한 후 작은 순서대로 돌아야하는데.. 계속 순서가 바뀌니까 어찌 해야할지 모르겠음 -> heapq쓰자
q = []
distances[X-1] = 0
heapq.heappush(q, (distances[X-1], X-1))
visited[X-1] = True
result = []
while q:
    dist, now_index = heapq.heappop(q)
    visited[now_index] = True
    if graph[now_index]:
        for next_index in graph[now_index]:
            if visited[next_index] == False and (dist+1) < distances[next_index]:
                distances[next_index] = (dist+1)
                heapq.heappush(q, (distances[next_index], next_index))
    if dist == K:
        result.append(now_index+1)

if result:
    result.sort()
    while result:
        print(result.pop(0))
else:
    print(-1)

'''
heapq 쓰면서 for문 썼더니 IndexError..
heappop을 N번 하게 될때 생기는 에러인듯.
heapq를 쓸거면 while문을, 직접 가장 작은 인덱스 매번 구하는 식으로 구현할거면 for문을 !

'''
