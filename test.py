N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

dp = [[-1]*101 for _ in range(N+1)]

def knapsack(idx, health):
    if idx == N or health <= 0:
        return 0
    
    if dp[idx][health] != -1:
        return dp[idx][health]
    
    result = knapsack(idx+1, health)
    
    if health > L[idx]:
        result = max(result, J[idx]+knapsack(idx+1, health-L[idx]))
    
    dp[idx][health] = result
    return result

print(knapsack(0,100))

# strength = 100
# def knapsack(strength, L, J, N):
#     k = [[0 for x in range(strength+1)] for x in range(N+1)]
#     for i in range(N+1):
#         for w in range(strength+1):
#             if i==0 or w==0:
#                 k[i][w] = 0
#             elif L[i-1] <= w:
#                 k[i][w] = max(J[i-1] + k[i-1][w-L[i-1]], k[i-1][w])
#             else:
#                 k[i][w] = 0
#     return k[N][strength]

# print(knapsack(100, L,J,N))