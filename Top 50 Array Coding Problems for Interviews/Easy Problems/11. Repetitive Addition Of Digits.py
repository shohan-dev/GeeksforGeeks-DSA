class Solution:
    def repeatedSumOfDigits (self,N):
        if N%9==0:
            return 9
        else:
            return N%9
