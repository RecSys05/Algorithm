# import sys
# input=sys.stdin.readline

# N=int(input())
# H=list(map(int,input().split()))
# H.sort()
# min_diff=float('inf')
# for p4 in range(3,N):
#     for p3 in range(2,p4):
#         for p2 in range(1,p3):
#             for p1 in range(0,p2):
#                 min_diff=min(min_diff,abs(H[p1]+H[p4]-H[p2]-H[p3]))

# print(min_diff)
# sort에서 시간초과 나나?

# import sys
# input=sys.stdin.readline

# N=int(input())
# H=list(map(int,input().split()))
# # H.sort()
# min_diff=float('inf')
# for p4 in range(3,N):
#     for p3 in range(2,p4):
#         for p2 in range(1,p3):
#             for p1 in range(0,p2):
#                 li=[H[p1],H[p2],H[p3],H[p4]] # O(1)
#                 li.sort() # O(1)
#                 min_diff=min(min_diff,abs(li[0]+li[3]-li[1]-li[2]))

# print(min_diff)

import sys
input=sys.stdin.readline

def main():
    N=int(input())
    H=list(map(int,input().split()))
    H.sort()
    min_diff=float('inf')
    for i in range(N-3):
        for j in range(i+3,N):
            left=i+1
            right=j-1
            while left<right:
                diff=H[i]+H[j]-H[left]-H[right]
                min_diff=min(min_diff,abs(diff))
                if diff>0:
                    left+=1
                elif diff<0:
                    right-=1
                else:
                    print(min_diff)
                    return
    print(min_diff)

main()