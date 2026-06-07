def coinChange(coins, amount):
    dp = [float("inf")] * (amount+1)
    dp[0] = 0

    for i in range(1, amount+1):
        for c in coins:
            if c<=i:
                dp[i] = min(dp[i], dp[i-c]+1)
    return dp[amount] if dp[amount] != float("inf") else -1

coins = [1,2,5]
amount = 8
print(coinChange(coins,amount))