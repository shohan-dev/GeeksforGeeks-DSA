class Solution:
    def getSecondLargest(self, a):
        a = set(a)           
        if len(a) < 2:       
            return -1
        a = list(a)          
        a.sort()
        return a[-2]         
