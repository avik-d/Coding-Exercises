
#https://leetcode.com/problems/partition-equal-subset-sum/submissions/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) is 0:
            return False
        
        sum = 0
        
        # If the sum is not divisible by 2, return False
        for i in range(0,len(nums)):
            sum += nums[i]    
        if (sum%2) != 0:
            return False
        
        #Target sum
        target = (int)(sum / 2)
        
        
        val = [[0 for i in range(len(nums)+1)] for j in range(target+1)] 
        for i in range(0,target+1):
            for j in range(0,len(nums)+1):
                if i is 0:
                    val[0][j] = True
                if j is 0:
                    val[i][0] = False
                    
        #val[0][0] = True
        for i in range(1,target+1):
            for j in range(1,len(nums)+1):
                #If weight of element is less than sum, we can either pick it or reject it
                if nums[j-1] <= i:
                    val[i][j] = val[i-nums[j-1]][j-1] or val[i][j-1]
                #If weight of element is greater than current sum, we can't pick it
                else:
                    val[i][j] = val[i][j-1]
        
        return val[target][len(nums)]
