import sys
n=int(input())

# bottom up
# 32544 KB
def dp1(n):
    if n <= 2:
        return n
    arr=[0]*(n+1) # 리스트 없이 변수 2개 선언하고 업데이트 해가면서 해도됨
              # top down 방식에서 사용하는 배열과는 다른 용도
              # 문제에 따라 0이아닌 float('inf') 또는 -1 등으로 채우는 경우가 있음
    # 기저
    arr[1]=1
    arr[2]=2
    # m1=1
    # m2=2
    # m3=0
    # 점화식
    # f(n)=f(n-1)+f(n-2)
    for i in range(3,n+1):
        arr[i]=(arr[i-1]+arr[i-2])%10007
        # m3=(m2+m1)%10007
        # m1=m2
        # m2=m3
        # m1 m2 m3
        #    |  |
        #    v  v
        #    m1 m2 m3
    return arr[n]
    # return m3

# top down 
# 32556 KB
sys.setrecursionlimit(10**6) # 파이썬 재귀 오류 원인
memo=[0]*(n+2) # n+1로 하면 n=1일 때 memo[2]에 접근하게 됨
# 기저
memo[1]=1
memo[2]=2
def dp2(n):
    if n<=2 or memo[n]!=0:
        return memo[n]
    # 점화식
    memo[n]=(dp2(n-1)+dp2(n-2))%10007 # memo[n]=memo[n-1]+memo[n-2] 안 됨.
    return memo[n]



print(dp2(n))