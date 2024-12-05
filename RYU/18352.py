import sys
from queue import PriorityQueue
input = sys.stdin.readline

edge={}
pq=PriorityQueue()
dis=[]
visited=[]

def add_edge(s,e):
    if s not in edge:
        edge[s]=[]
    edge[s].append(e)

def dij(e):
    dis[e]=0
    pq.put([dis[e],e])

    while not pq.empty():
        d,n=pq.get()
        if visited[n]:
            continue
        visited[n] = True
        # print(f"get ({d},{n})")
        if n in edge:
            for node in edge[n]:
                dis[node]=min(dis[node],d+1)
                pq.put([dis[node],node])
                # print(f"put ({dis[node]},{node})")
    return


N, M, K, X = map(int,input().split())
# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
dis=[float('inf')]*(N+1)
visited=[False]*(N+1)
for i in range(M):
    s,e=map(int,input().split())
    add_edge(s,e)
dij(X)
ans=[i for i, x in enumerate(dis) if x == K]
if ans:
    print(*ans)
else:
    print(-1)


'''
시간초과
-> visited flag 추가하여 해결
'''