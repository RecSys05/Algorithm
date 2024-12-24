import sys
input=sys.stdin.readline

n=int(input())
li=[]
for i in range(n):
    l=int(input())
    li.append(l)
cmd=[]
st=[]
p=1
possible=True
for i in range(n):
    while not li[i]<p:
        st.append(p)
        cmd+=['+']
        p+=1
    if st[-1]==li[i]:
        st.pop()
        cmd+=['-']
    else:
        possible=False
        break
if possible:
    for i in range(len(cmd)):
        print(cmd[i])
else:
    print('NO')





# p1=0
# p2=n-1
# k=1
# possible=True
# for i in range(0,n):  
#     if li[i]==li[i-1]-1:
#         pass
#     else:
#         # a=i-p1
#         while li[p2]==li[p2-1]-1:
#             p2-=1
#         while li[p1]==li[p1+1]+1:
#             p1+=1
# while p1!=p2:
#     while li[p2]==li[p2-1]-1:
#         p2-=1
#     while li[p1]==li[p1+1]+1:
#         p1+=1
#     if li[p1]==li[p2]+1:
#         p1+=1
#         p2-=1
#     else:
#         possible=False
#         break


# pushstart=li[0]
# last=0
# npop=1
# nplus=0
# nminus=0
# cmd=[]

# for i in range(1,n):
#     if li[i]!=li[i-1]-1:
#         cmd+=['+']*(pushstart-last)
#         nplus+=pushstart-last
#         last=pushstart
#         pushstart=li[i]
#         cmd+=['-']*npop
#         nminus+=npop
#         npop=0
#     npop+=1
#     if nplus==n:
#         cmd.append(['-']*(n-nminus))
#         break
# print(*cmd)



# 43 6 87 5 21
# 43  ++++--
# 6   ++-
# 8   ++
# 7   -
# 521 ---

#12534