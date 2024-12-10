import sys
input=sys.stdin.readline
N=int(input()) # 5
P=list(map(int,input().split()))# 10 9 8 7 6
PP=[-1]+P

# bottom-up
# 여기의 배열(cost)은 지속적으로 업데이트됨
cost=PP
if N==1:
    print(PP[1])
else:    
    for i in range(2,N+1):
        for j in range(1,i//2+1):
            cost[i]=max(cost[i],cost[j]+cost[i-j])
    print(cost[N])

# top-down
# 여기의 배열(memo)은 '-1'에서 한 번 업데이트된 값이 고정됨
# 최대값이 확실할 때 메모
memo=[-1]*(N+1)
memo[1]=PP[1]
def dp(N):
    if N==1 or memo[N]!=-1:
        return memo[N]
    result=PP[N]
    for i in range(1,N//2+1):
        result=max(result,dp(i)+dp(N-i))
    memo[N]=result
    return memo[N]
print(dp(N))