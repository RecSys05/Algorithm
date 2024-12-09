import sys
input=sys.stdin.readline
N=int(input()) # 5
P=list(map(int,input().split()))# 10 9 8 7 6
PP=[-1]+P
cost=PP
if N==1:
    print(PP[1])
else:    
    for i in range(2,N+1):
        for j in range(1,i//2+1):
            cost[i]=max(cost[i],cost[j]+cost[i-j])
    print(cost[N])