
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) is 1:
            return 1
        if len(s) is 0:
            return 0;
        
        # i is start index
        # j is current end index
        # We have already identified string to be of length 2
        i = 0
        j = 1
        maxlen = 1
        
        
        # visited array will hold if we have already seen an element
        # We have already considered first elemt, so mark it as visited
        visited = [False]*256
        visited[ord(s[0])] = True
        
        #Algorithm:
        # 1. Until we find unvisited element, keep extending j
        # 2. As soon as we find a visited elemen, mark that element as False and increment i
        # Loop over the whole string
        while (j<len(s)):
            if visited[ord(s[j])] is False:
                visited[ord(s[j])] = True
                maxlen = max(maxlen, j - i + 1)
                print(i)
                print(j)
                j = j + 1
            else:
                visited[ord(s[i])] = False
                i = i + 1
        return maxlen
            
        
