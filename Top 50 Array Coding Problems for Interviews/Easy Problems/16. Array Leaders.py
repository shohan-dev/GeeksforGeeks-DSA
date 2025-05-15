class Solution:
    def leaders(self, a):
        max_val = -1
        final = []
        for i in range(len(a)-1,-1,-1):
            if max_val <= a[i]:
                final.append(a[i])
                max_val = a[i]
        
        final.reverse()
        return final