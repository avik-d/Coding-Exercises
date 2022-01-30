this is same as print subsets stuff.
Need to keep track of left and right parenthesis and recur

class Solution:
    def myPren(self, leftcount, rightcount, index, mylist,mystr):
        if ((leftcount < 0) or (rightcount < leftcount)):
            return
 
        if ((leftcount == 0) and (rightcount == 0)):
            mylist.append("".join(mystr))
            return
        
        mystr[index]='('
        self.myPren(leftcount-1, rightcount, index+1, mylist, mystr)
        
        mystr[index]=')'
        self.myPren(leftcount, rightcount-1, index+1, mylist, mystr)
    
    def generateParenthesis(self, n: int) -> List[str]:
        mylist = []
        mystr = ["" for i in range(2*n)] 
        self.myPren(n,n,0,mylist,mystr)
        return mylist
