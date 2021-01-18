class Solution:

    history = [[1, 1, 1, 1, 1]]
    
    def countVowelStrings(self, n: int) -> int:
        while(len(self.history) < n):
            self.getNext()
        return sum(self.history[n - 1])
                

    def getNext(self):
        lastIndex = len(self.history) - 1
        newItem = [1]
        newItem.append(newItem[0] + self.history[lastIndex][1])
        newItem.append(newItem[1] + self.history[lastIndex][2])
        newItem.append(newItem[2] + self.history[lastIndex][3])
        newItem.append(newItem[3] + self.history[lastIndex][4])
        self.history.append(newItem)
            
