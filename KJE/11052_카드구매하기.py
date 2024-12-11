import sys
input = sys.stdin.readlines
user_input = input()

n = int(user_input[0])
p = list(map(int, user_input[1].split()))

p.insert(0,0)
print(p)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i], p[j] + dp[i-j])
print(dp[n])