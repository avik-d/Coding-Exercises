#Leetcode submission - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/


class Solution:
    def myfunc(self,nums,low,high,minelem):
        if low > high:
            return
        mid = (high+low)//2
        
        #Check if arr[low]...arr[mid] is sorted
        #Then minimum element in arr[low]....arr[mid] must be arr[low]
        #keep a note of minimum and recur for arr[mid+1].....arr[high]
        if nums[low] <= nums[mid]:
            if len(minelem) == 1:
                minelem[0]=min(minelem[0],nums[low])
            else:
                minelem.append(nums[low])
            self.myfunc(nums,mid+1,high,minelem)
        
        #else arr[mid]....arr[high] must be sorted
        else:
            if len(minelem) is 1:
                minelem[0]=min(minelem[0],nums[mid])
            else:
                minelem.append(nums[mid])
            self.myfunc(nums,low,mid-1,minelem)
    def findMin(self, nums: List[int]) -> int:
        minelem = []
        self.myfunc(nums,0,len(nums)-1,minelem)
        return minelem[0]
        
