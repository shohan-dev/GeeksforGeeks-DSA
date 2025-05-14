class Solution:
    def reverseInGroups(self, arr, k):
        for i in range(0,len(arr)-1,k):
            arr[i:i+k] = reversed(arr[i:i+k])
        return arr