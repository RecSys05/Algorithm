import sys
input = sys.stdin.readlines
user_input = input()
N = int(user_input[0])
parti = list(i.strip() for i in user_input[1:N+1])
done = list(i.strip() for i in user_input[N+1:])

# 0. dict로 풀기
all_dict = {}
for one in parti:
    if one in all_dict:
        all_dict[one] += 1
    else:
        all_dict[one] = 1

for one in done:
    all_dict[one] -= 1

for name, num in all_dict.items():
    if num:
        print(name)
        break


# 1. list-count로 풀기 - 시간초과
# all = parti + done

# for index, value in enumerate(parti):
#     num = all.count(value)
#     if num %2 == 1:
#         print(value)
#         break


# 2. pop으로 풀기 - 실패
# result = parti.copy()
# for one in done:
#     for index, value in parti:
#         if one == value:
#             result.pop(index)


'''
새로 알게 된 점
1. 'dict[key] = value' 형태로 딕셔너리에 key, value 추가
2. 딕셔너리에 key랑 value가 하나라도 있는 후에는 + -를 통해 value를 추가하거나 제거할 수 있음
3. 'dict.items()'를 통해 key와 value 쌍을 뽑을 수 있다.
4. list의 count 매서드를 이용하면 개수를 세어 줌
'''