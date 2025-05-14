class Solution:
    def maxConsecutiveCount(self, arr):
        #code here 
        one =0
        zero =0
        for i in arr:
            if i==1:
               one+=1
            else:
                zero+=1
        return max(one,zero)
