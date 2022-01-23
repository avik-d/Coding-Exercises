https://leetcode.com/problems/product-of-array-except-self/submissions/
Algorithm:
  1. create prefix product array
  2. Create postfix prodcut array
  3. For answe, answer[i] will be pre[i-1]*post[i+1]
  4. Handle pre and post seperately
  
  class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preproduct = []
        postproduct = []
        presum  = 1
        postsum = 1
        
        #Calculate the prefix product
        for i in range(0,len(nums)):
            presum = presum * nums[i]
            preproduct.append(presum)
        
        #Calculate the postfix product
        i = len(nums)-1
        while (i >=0):
            postsum = postsum * nums[i]
            postproduct.append(postsum)
            i = i -1
        postproduct.reverse()
        
        #Compose the output
        output=[]
        val = 1
        output.append(postproduct[1])
        for i in range(1,len(nums)-1):
            output.append(preproduct[i-1]*postproduct[i+1])
        output.append(preproduct[len(nums)-2])
        return output
            
        
        
