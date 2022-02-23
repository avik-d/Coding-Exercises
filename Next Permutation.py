
https://leetcode.com/problems/next-permutation/submissions/

# Step -1 : Find the first element such that a[i] < a[i+1] : Let's call it index 1
# Step 2:   Again start scan from end and find the first elemnt that is > a[i]: Let's call it index 2
# Step 3:   Swap ind1 and ind2
# Step 4 :  Reverse arr(ind+1..last) 

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)
        if l <= 1:
            return nums
        
        ind1 = -1
        ind2 = -1
        
        
        # Step - 1
        i = l -1
        while(i > 0):
            if nums[i] > nums[i-1]:
                ind1 = i-1
                break
            i = i - 1
        
        # Step - 1A. If no such element found just return the reverse
        # This will be the case if the array is reverse sorted, for example [3,2,1]
        if ind1 == -1:
            nums = nums.reverse()
            return
        
        # Step - 2
        i = l - 1
        while (i > 0):
            if nums[i] > nums[ind1]:
                ind2 = i
                break
            i = i - 1
        
        
        # Step - 3 
        nums[ind1],nums[ind2] = nums[ind2],nums[ind1]
        
        
        #Step - 4 
        i = ind1 + 1
        j = len(nums)-1
        while (i <= j):
            nums[i],nums[j] = nums[j],nums[i]
            i = i + 1
            j = j - 1

            
        
