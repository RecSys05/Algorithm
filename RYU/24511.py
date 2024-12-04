import sys
input=sys.stdin.readline

'''
N=int(input())# 4
A=list(map(int, input().split()))# 0110 0은 큐, 1은 스택
b=list(map(int, input().split()))# 1234
B=[[e] for e in b]# [[1],[2]]
M=int(input())# 3
C=list(map(int, input().split()))# 247

ans=[]

for c in C:
    nextE=c
    for i in range(N):
        B[i].append(nextE)
        if A[i] == 0:
            nextE=B[i].pop(0)
        else:
            nextE=B[i].pop()
    ans.append(nextE)

for a in ans:
    print(a)
'''

'''
N=int(input())# 4
A=list(map(int, input().split()))# 0110 0은 큐, 1은 스택
B=list(map(int, input().split()))# 1234
M=int(input())# 3
C=list(map(int, input().split()))# 247

queue = []
for i in range(N-1, -1, -1):
    if A[i] == 0:
        queue.append(B[i])

ans = []
for c in C:
    queue.append(c)
    ans.append(queue.pop(0))

for a in ans:
    print(a)
'''

'''
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue = deque()
for i in range(N-1, -1, -1):
    if A[i] == 0:
        queue.append(B[i])

ans = []
for c in C:
    queue.append(c)
    ans.append(queue.popleft())

print(*ans) 
'''

'''
둘 다 시간 초과 -> queue.pop(0)의 시간 복잡도가 O(n)이기 때문에
'''


N=int(input())# 4
A=list(map(int, input().split()))# 0110 0은 큐, 1은 스택
B=list(map(int, input().split()))# 1234
M=int(input())# 3
C=list(map(int, input().split()))# 247

queue = []
for i in range(N-1, -1, -1):
    if A[i] == 0:
        queue.append(B[i])

ans=queue+C

for a in ans[:M]:
    print(a)