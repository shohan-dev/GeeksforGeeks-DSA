class Solution:

    def addOne(self, arr):
        n = len(arr)
        for i in range(n - 1, -1, -1):

            if arr[i] < 9:
                arr[i] += 1
                return arr

            arr[i] = 0
            
        return [1] + [0] * n
