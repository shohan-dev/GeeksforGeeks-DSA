class Solution:
    def missingRanges(self, a, lower, upper):
        final = []
    
        if a[0] > lower:
            final.append([lower, a[0] - 1])
        
        for i in range(len(a) - 1):
            if a[i+1] - a[i] > 1:
                final.append([a[i] + 1, a[i+1] - 1])
        
        if a[-1] < upper:
            final.append([a[-1] + 1, upper])

        return final