/* 
Your task is to count the number of ways to construct sum n by throwing a dice one or more times. Each throw produces an outcome between 1 and 6.
*/

n = int(input())
m = 1000000007
dp = [0] * n 
#print(dp)
dp[0] = 1
for i in range(0,n):
    for x in range(0,6):
        if(x>i):
            break
        #print(i,x)
        dp[i] = (dp[i]+dp[i-x]) % m
print(dp[n-1])
