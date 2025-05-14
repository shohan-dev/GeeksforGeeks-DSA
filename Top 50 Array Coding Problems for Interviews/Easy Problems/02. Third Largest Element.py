class Solution:
    def thirdLargest(self, a):
        if len(a) ==2:
            return -1
        if len(a) == 1:
            return a[0]
        a = list(a)
        a.sort() 
        return a[-3]  