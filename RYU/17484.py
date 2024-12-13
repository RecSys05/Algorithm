import sys
input=sys.stdin.readline

N,M=map(int,input().split())

space=[]
for n in range(N):
    li=list(map(int,input().split()))
    space.append(li)

# 3차원 배열
memo = [[[float('inf')]*3 for _ in range(M + 2)] for _ in range(N + 1)]
# dir = [float('inf')] * 3
# row = dir * (M + 2)
# memo = row * (N + 1)
for n in range(1,N+1):
    for m in range(1,M+1):
        if n==1:
            memo[n][m][0]=space[n-1][m-1]
            memo[n][m][1]=space[n-1][m-1]
            memo[n][m][2]=space[n-1][m-1]
        else:
            memo[n][m][0]=space[n-1][m-1]+min(memo[n-1][m-1][1],memo[n-1][m-1][2])
            memo[n][m][1]=space[n-1][m-1]+min(memo[n-1][m][0],memo[n-1][m][2])
            memo[n][m][2]=space[n-1][m-1]+min(memo[n-1][m+1][0],memo[n-1][m+1][1])

# 2차원 배열 최솟값
min_fee = min(map(min, memo[N]))
print(min_fee)