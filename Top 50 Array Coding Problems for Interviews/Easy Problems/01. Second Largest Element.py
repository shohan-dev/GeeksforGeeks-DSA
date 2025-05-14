class Solution:
    def getSecondLargest(self, a):
        a = set(a)           # remove duplicates
        if len(a) < 2:       # less than 2 unique elements
            return -1
        a = list(a)          # convert set to list
        a.sort()
        return a[-2]         # second largest

