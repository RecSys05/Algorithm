import sys
import heapq
input=sys.stdin.readline

N=int(input())
li=[]
# total=0
som=-int(input())
for i in range(N-1):
    voter=-int(input())
    # total+=voter
    heapq.heappush(li,voter)

count=0
while True:
    if not li: # li empty -> IndexError
        break
    maxV=li[0]
    if som<maxV:
        break
    som-=1
    heapq.heappop(li)
    heapq.heappush(li,maxV+1)
    count+=1

print(count)

'''
goal=int(total/N)+1
if goal>li[0]:
    print(goal-li[0])
else:
    print(0)
'''

