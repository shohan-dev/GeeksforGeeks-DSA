class Solution:
    def rearrange(self,arr):
        pos , neg = [],[]

        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        
        # pos,neg
        p =0
        s = min(len(pos),len(neg))
        m = max(len(pos),len(neg))
        
        final =[]
        for i in range(s):
            final.append(pos[i])
            final.append(neg[i])
            p +=1
        
        final.extend(pos[p:])
        final.extend(neg[p:])
        
        for i in range(len(final)):
            arr[i] = final[i]
        return arr  