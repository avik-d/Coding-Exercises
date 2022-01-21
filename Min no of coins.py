#Algo
1. OUTER LOOP - Run for all amounts
2. ways[i] = Minimum number of cois needed to make i amount


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ways = [sys.maxsize]*(amount + 1)
        ways[0] = 0
        for i in range(1,amount+1):
            for j in range(0,len(coins)):
                if (coins[j]<=i):
                    ways[i] = min(ways[i], 1 + ways[i-coins[j]])
        
        if ways[amount] is sys.maxsize:
            return -1
        else:
            return ways[amount]
            
        
