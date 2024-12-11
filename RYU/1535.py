import sys
input=sys.stdin.readline

N=int(input())
L=list(map(int,input().split())) # 체력
L=[0]+L
J=list(map(int,input().split())) # 기쁨
J=[0]+J
lim=99

def knapsack(N,L,J,lim):
    arr=[[0 for x in range(lim+1)] for x in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,lim+1):
            if L[i]<=j:
                arr[i][j]=max(arr[i-1][j],J[i]+arr[i-1][j-L[i]])
            else:
                arr[i][j]=arr[i-1][j]
    return arr[N][lim]

print(knapsack(N,L,J,lim))