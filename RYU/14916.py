import sys
sys.setrecursionlimit(10**6)

# memo={1:-1, 2:1, 3:-1, 4:2, 5:1}
# def exchange(n):
#     if n in memo:
#         return memo[n]
#     e5=exchange(n-5)
#     e2=exchange(n-2)
#     if e5==-1 and e2==-1:
#         memo[n]=-1
#     elif e5!=-1 and e2!=-1:
#         memo[n]=min(e5,e2)+1
#     else:
#         memo[n]=e5+e2+1+1
#     return memo[n]

# n=int(input())
# print(exchange(n))

'''
13 -> 거스를 수 있다면 
13-5=8 또는 13-2=11
'''
memo={1:float('inf'), 2:1, 3:float('inf'), 4:2, 5:1}
def exchange(n):
    if n in memo:
        return memo[n]
    e5=exchange(n-5)
    e2=exchange(n-2)
    memo[n]=min(e5,e2)+1
    return memo[n]
n=int(input())
e=exchange(n)
if e!=float('inf'):
    print(e)
else:
    print(-1)
