https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/800/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Build a heap - O(n)
        myheap = []
        for i in range(0,len(nums)):
            myheap.append(-nums[i])
        heapify(myheap)
        print(myheap)
        
        #Pop item k-1 times, time: (k-1)*logn ~= klogn
        for i in range(0,k-1):
            heappop(myheap)
        
        #Time complexity - Klogn
        return -myheap[0]
