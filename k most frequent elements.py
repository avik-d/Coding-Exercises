#Leetcode link - https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for i in range(0,len(nums)):
            if nums[i] not in m:
                m[nums[i]] = 1
                continue
            else:
                m[nums[i]] += 1
                continue
        
        #Build a Max heap - This step takes O(n) time
        myheap = []
        for num, frequency in m.items():
            myheap.append((-frequency, num))
        heapify(myheap)
        
        #Pop k times and return that in a list
        #Popping k time will take O(klogn) time in total
        returnlist = []
        for i in range(0,k):
            num = heappop(myheap)[1]
            returnlist.append(num)
        
        return returnlist
            
                
        
            
        
