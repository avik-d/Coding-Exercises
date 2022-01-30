https://leetcode.com/problems/longest-increasing-subsequence/submissions/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longestSubsequence=[1 for i in range(len(nums))]
        if (len(nums)<=1):
            return len(nums)
        
        for i in range(1,len(nums)):
            for j in range(0,i):
                if (nums[i] > nums[j]) and longestSubsequence[i]<longestSubsequence[j]+1:
                    longestSubsequence[i] = longestSubsequence[j]+1
        
        print(longestSubsequence)
        return max(longestSubsequence)
