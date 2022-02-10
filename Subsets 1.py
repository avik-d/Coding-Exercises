Leetcode link - https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/796/
  1. Pick a problem and recur
  2. Don't pick an element and recur
  3. Time complexity is O(2^n) as we can either pick an element or may not

class Solution:
    def printcode(self,num,index,returnlist,cur):
        if index >= len(num):
            #list([]) creates a copy of list
            # We should create a copy of cur, else everything will change
            returnlist.append(list(cur))
            return
        
        #Include the element and recur
        cur.append(num[index])
        self.printcode(num,index+1,returnlist,cur)
        
        #Do not include the next element and recur 
        cur.pop()
        self.printcode(num,index+1,returnlist,cur)
        
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        returnlist = []
        curlist = []
        self.printcode(nums,0,returnlist,curlist)
        return returnlist
        
