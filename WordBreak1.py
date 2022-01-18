#https://leetcode.com/problems/word-break/submissions/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # This is the dp array that will hold the solution
        # dp[i] is True if string of length 0.....i can be segmented into dictionary words
        dp = [False for i in range(0, len(s) + 1)]
        # print(dp)
        dp[0] = True

        # Loop over the length of the string
        # In the inner loop run from start of the string to current length
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if dp[j] is True and s[j:i] in wordDict:
                    dp[i] = True
                    break  # Important, because we found a solution, running over all possible break might return false.
        return dp[len(s)]

        # Time complexity - O(n3) ** 2 inner loopds and another check made in the dict
        # Space complexity - O(n)
