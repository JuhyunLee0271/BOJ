s1 = list(input())
s2 = list(input())

dp = [[""] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        if s1[j-1] == s2[i-1]: 
            dp[i][j] = dp[i-1][j-1] + s1[j-1]

        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[len(s2)][len(s1)]))
print(dp[len(s2)][len(s1)]) 