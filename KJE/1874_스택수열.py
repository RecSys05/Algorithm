import sys
input = sys.stdin.readlines
user_input = input()
N = int(user_input[0])
arr = list(int(i) for i in user_input[1:])

cnt = 1
stack = []
result = []
breaking_point = True
for num in arr:
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        result.append('+')
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        breaking_point = False
        break

if breaking_point:
    for i in result:
        print(i)
else:
    print("NO")

'''
보완할 점
다른 친구들의 코드를 보니 print("\n".join(result))를 실행해서 마지막 for문을 돌지 않고도 쭉 print할 수 있음을 알았다.
'''