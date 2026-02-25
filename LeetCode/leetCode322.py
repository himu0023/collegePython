def checkCoin(nums, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for a in range(1, amount+1):
        for i in nums:
            if a - i >=0:
                dp[a] = min(dp[a], 1+dp[a-i])
    return dp[amount] if dp[amount]!=amount+1 else -1



nums = [1,3,4,5]
amount = 2

x = checkCoin(nums, amount)
print(x)