Leetcode lnk - https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/823/
Algo:
  1. Push elements
  2. If operator is encountered, pop top 2 elements and then push back on to the stack
  3. See how floor() and ceil() works

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mystack = []
        for i in range(0,len(tokens)):
            if tokens[i] not in ["+","-","*","/"]:
                mystack.append(int(tokens[i]))
            else:
                top1 = mystack[len(mystack)-1]
                top2 = mystack[len(mystack)-2]
                mystack.pop()
                mystack.pop()
                if tokens[i] is "+":
                    mystack.append(top1 + top2)
                if tokens[i] is "-":
                    mystack.append(top2 - top1)
                if tokens[i] is "*":
                    mystack.append(top1 * top2)
                if tokens[i] is "/":
                    if top2/top1 <0:
                        mystack.append(math.ceil(top2 / top1))
                    else:
                        mystack.append(math.floor(top2 / top1))
        return mystack[0]
                
        
