
1. The video lecture to view: https://www.youtube.com/watch?v=YK78FU5Ffjw&list=PLgUwDviBIf0p4ozDR_kJJkONnb1wdx2Ma&index=56&t=0s&ab_channel=takeUforward
2. My Solution - https://leetcode.com/problems/permutations/submissions/
    
    
    How does this work?
    1. We create a map like data structure (freq) that helps us in picking what can be picked and is not already picked
    2. Then we pick that element and recur
    3. When "ds" becomes length of string, we add to result
    4. We rmeove the last element from recursion stack
    
    
    class Solution:
    def permRec(self,nums,freq,ds,ans):
        #Base case : If we hae reached string length, done
        if len(ds) is len(nums):
            ans.append(list(ds))#Very very important - I missed this conversion to do list()
            #print(ans)
            return
            
        for i in range(0,len(nums)):
            if freq[i] is False:  #If this element can be picked
                ds.append(nums[i])
                freq[i]= True
                self.permRec(nums,freq,ds,ans)
                #IMP - After processing, remove from ds and freq
                ds.pop()
                freq[i]=False
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #Map to hold which elements are currently selected
        freq = [False for i in range(0,len(nums))]
        
        #Data structure to hold the current answer
        ds = []
        
        #The list that will hold all the permutations
        ans = []
        self.permRec(nums,freq,ds,ans)
        return ans
        
    
