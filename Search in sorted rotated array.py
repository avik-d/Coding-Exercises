#Leetcode link: https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/

#Algorithm:
#1) Find middle point mid = (l + h)/2
#2) If key is present at middle point, return mid.
#3) Else If arr[l..mid] is sorted
    #a) If key to be searched lies in range from arr[l] to arr[mid], recur for arr[l..mid].
    #b) Else recur for arr[mid+1..h]
#4) Else (arr[mid+1..h] must be sorted)
    #a) If key to be searched lies in range from arr[mid+1] to arr[h], recur for arr[mid+1..h].
    #b) Else recur for arr[l..mid]  

class Solution:
    
    def myfunc(self,nums,low,high,key):
        if low>high:
            return -1
        mid = (high+low)//2
        if nums[mid] == key:
            return mid
        
        # If arr[l...mid] is sorted
        if nums[low]<=nums[mid]:
            # As this subarray is sorted, we can quickly
            # check if key lies in half or other half
            if key>=nums[low] and key<=nums[mid]:
                return self.myfunc(nums,low,mid-1,key)
            return self.myfunc(nums,mid+1,high,key)
        
        # If arr[l..mid] is not sorted, then arr[mid... r]
        # must be sorted
        else:
            if key>=nums[mid] and key<=nums[high]:
                return self.myfunc(nums,mid+1,high,key)
            return self.myfunc(nums,low,mid-1,key)
    
    def search(self, nums: List[int], target: int) -> int:
        return self.myfunc(nums,0,len(nums)-1,target)
