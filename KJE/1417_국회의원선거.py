import sys
import heapq

input = sys.stdin.readlines
user_input = input()
N = int(user_input[0])
dasom = -int(user_input[1])
candidates = [-i for i in list(map(int, user_input[2:]))]

heapq.heapify(candidates)

def mesu(winner, others):
    if not others:
        return 0
    
    plus_vote = 0
    while winner >= min(others):
        candidate = heapq.heappop(others)
        heapq.heappush(others, int(candidate+1))
        winner -= 1
        plus_vote += 1
    return plus_vote

print(mesu(dasom, candidates))

'''
새로 알게 된 점
1. int 앞에 "-"해도 음수 적용이 되는구나
2. 단순히 리스트를 만들어서는 heap으로 인지하지 못함. heapify를 통해 heap으로 만들어주어야 매서드 사용 가능
**3. heappop은 최소 값을 pop함. 그래서 최대 힙을 구현하기 위해서는 "음수" 값으로 바꾼 후 진행해야함
4. pop할때는 항상! 리스트가 empty하게 되는 경우는 없는지 확인해주어야 함

보완할 점
다른 친구들의 코드를 보니 while문 조건으로 heap에 원소가 있는 경우 ~~ 를 넣은 것을 확인할 수 있음. 이것으로 한다면 내 코드에서 if문을 삭제할 수 있을 것으로 보임. 
앞으로는 heap을 쓸때 "while heap:" 으로 작성해보자.
'''