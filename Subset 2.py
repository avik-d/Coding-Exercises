#Leetcode : https://leetcode.com/problems/subsets-ii/submissions/

class Solution:
    def printcode(self,num,index,returnlist,cur):
        if index >= len(num):
            returnlist.append(list(cur))
            return
        
        #Include the element and recur
        cur.append(num[index])
        self.printcode(num,index+1,returnlist,cur)
        
        #Do not include the next element and recur 
        #Idea is if we do not include i th element,then skip duplicate elements
        cur.pop()
        while (index+1<len(num) and num[index] == num[index+1]):
            index = index +1
        self.printcode(num,index+1,returnlist,cur)
        
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        returnlist = []
        curlist = []
        nums = sorted(nums)
        self.printcode(nums,0,returnlist,curlist)
        return returnlist
