The algorithm is in the code comments itself.
LeetCode link : https://leetcode.com/problems/merge-intervals/submissions/

class Solution:
    
    # My custom sort function
    def mysort(self,listelem):
        return listelem[0]
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:
            return intervals
        final=[]
        
        #Sort the given array based on the start time
        current=sorted(intervals,key=self.mysort)
        
        # The first element should be in the answer
        final.append(current[0])
        
        for i in range (1, len(current)):
            currentelem = current[i]
            currentstart = currentelem[0]
            currentend = currentelem[1]
            
            # If current elem end is gretaer than last inspected element's end
            # and current elemen't start is less than last inspected element's start,
            # merge these 2 elements
            if currentend > final[len(final)-1][1]:
                if currentstart <= final[len(final)-1][1]:
                    final[len(final)-1][1] = currentend
                    
                #else just add the element
                else:
                    final.append([currentstart,currentend])
        return final
