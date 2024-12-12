import sys
input = sys.stdin.readline
N=int(input())
name_dict={}
for i in range(N):
    name=input()
    if name in name_dict:
        name_dict[name]+=1
    else:
        name_dict[name]=1
for i in range(N-1):
    name=input()
    name_dict[name]-=1
for name, count in name_dict.items():
    if count > 0:
        print(name)
        break

# input = sys.stdin.readline 쓰니까 시간초과 안 남;;
# 43164KB	132ms

'''
import sys
input = sys.stdin.readline
N=int(input())
name_dict={}
for i in range(N):
    name=input()
    if name in name_dict:
        name_dict[name]+=1
    else:
        name_dict[name]=1
som=''
for i in range(N-1):
    name=input()
    if name_dict[name]==1:
        som=name
    name_dict[name]-=1
print(som)

# dict(내장 자료형)를 변수명으로 써서 오류
# 모든 참가자가 동명이인인 경우만 가능
'''

'''
import sys
input = sys.stdin.readline
N = int(input())
participants = set()

for _ in range(N):
    name = input()
    if name in participants:
        participants.remove(name)
    else:
        participants.add(name)

for _ in range(N - 1):
    name = input()
    if name in participants:
        participants.remove(name)
    else:
        participants.add(name)

print(participants.pop())

# 미완주자가 한 명임이 보장되기 때문에 가능함
'''

'''
import sys
input = sys.stdin.readline
N = int(input())
participants = set()

for _ in range(N*2-1):
    name = input()
    if name in participants:
        participants.remove(name)
    else:
        participants.add(name)

print(participants.pop())

# 43680KB	124ms
'''