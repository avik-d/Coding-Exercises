#https://leetcode.com/problems/word-ladder/submissions/

#Important things to note:
# Think to understand why BFS always gives the shortest path

class Solution:
    def myfunc(self,beginWord,endWord,wordList,queue):
        wordList = set(wordList)
        while(len(queue) > 0):
            curWord,curDepth = queue.popleft()
            curWordLength = len(curWord)
            if curWord == endWord:
                return curDepth+1
            for i in range(0,curWordLength):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = curWord[0:i]+j+curWord[i+1:curWordLength]
                    if newWord in wordList:
                        queue.append((newWord,curDepth+1))
                        wordList.remove(newWord)
        return 0

    
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = collections.deque([])
        queue.append((beginWord,0))
        return self.myfunc(beginWord,endWord,wordList,queue)
