import sys
input = sys.stdin.readlines
user_input = input()
N, M = list(map(int,user_input[0].split()))

hear_set = set(i.strip() for i in user_input[1:N+1])
see_set = set(i.strip() for i in user_input[N+1:])

hear_see_set = hear_set.intersection(see_set)
hear_see_list = list(hear_see_set)
hear_see_list.sort()
print(len(hear_see_list))
for hear_see in hear_see_list:
    print(hear_see)

'''
보완할 점
sorted(hear_see_set)하면 리스트로 바꾸고 정렬해서 반환하므로 따로 list로 만드록 sort할 필요 없어짐

hear_see_set = hear_set.intersection(see_set)
hear_see_list = sorted(hear_see_set)
'''