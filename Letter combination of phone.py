# Leetcode solution - https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/
idea:
1. maintain curindex
2. loop over all possible characters for every digit

class Solution:
    def myrecur(self,curindex,curstring,digit_to_number,digits,returnlist):
        if len(curstring) == len(digits):
            returnlist.append(curstring)
            return
        for c in digit_to_number[digits[curindex]]:
            self.myrecur(curindex+1,curstring+c,digit_to_number,digits,returnlist)
            
            
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_number = {}
        digit_to_number["2"] = "abc"
        digit_to_number["3"] = "def"
        digit_to_number["4"] = "ghi"
        digit_to_number["5"] = "jkl"
        digit_to_number["6"] = "mno"
        digit_to_number["7"] = "pqrs"
        digit_to_number["8"] = "tuv"
        digit_to_number["9"] = "wxyz"
        
        if len(digits) is 0:
            return []
        
        returnlist=[]
        self.myrecur(0,"",digit_to_number,digits,returnlist)
        return returnlist
