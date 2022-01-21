# Time Complexity - O(n2)
# Space complexity - O(1)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <=1:
            return s[0:len(s)]
        maxodd = 1
        maxeven = 0
        maxoddstart = 0
        maxoddend = 0
        maxevenstart = 0
        maxevenend = 0
        
        #Generate all odd length palindromes
        for i in range(1,len(s)):
            start = i-1
            end = i + 1
            curmax = 1
            while ( start >=0 and end<len(s)):
                if s[start] is s[end]:
                    start = start - 1
                    end = end + 1
                    continue
                else:
                    break
            if ((end-1)-(start+1)+1) > maxodd:
                maxodd = ((end-1)-(start+1)+1)
                maxoddstart = start + 1
                maxoddend = end -1
            
        #Generate all even length palindromes
        # Tricky - For even length, start from 0
        for i in range(0,len(s)):
            start = i
            end = i + 1
            while ( start >=0 and end<len(s)):
                if s[start] is s[end]:
                    start = start - 1
                    end = end + 1
                    continue
                else:
                    break
            if ((end-1)-(start+1)+1) > maxeven:
                maxeven = ((end-1)-(start+1)+1)
                maxevenstart = start + 1
                maxevenend = end -1
                
        if maxodd > maxeven:
            return s[maxoddstart:maxoddend+1]
        else:
            return s[maxevenstart:maxevenend+1]
