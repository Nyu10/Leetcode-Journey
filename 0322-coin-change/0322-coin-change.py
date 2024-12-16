
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =[-1] * (amount + 1)
        dp[0] = 0
        for i in range(0, amount+1):
            for coin in coins:
                if i-coin >=0 and dp[i-coin] != -1:
                    dp[i] = 1 + dp[i-coin]
        print(dp)
        return dp[amount]