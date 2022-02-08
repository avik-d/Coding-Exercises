# Video Explanation - https://www.youtube.com/watch?v=qhBVWf0YafA&t=19s&ab_channel=NeetCode

# Leetcode link - https://leetcode.com/problems/permutations-ii/submissions/
class Solution:
    def myfunc(self,nums,freq,curString,returnList):
        if len(curString) == len(nums):
            returnList.append(curString.copy())
            return
        for i in freq.keys():
            if freq[i] > 0:
                curString.append(i)
                freq[i] -= 1
                self.myfunc(nums,freq,curString,returnList)
                curString.pop()
                freq[i] += 1
    
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        #print(freq.keys())
        curString = []
        returnList = []
        self.myfunc(nums,freq,curString,returnList)
        return returnList
