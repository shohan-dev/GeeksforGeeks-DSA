class Solution:
    def maxProduct(self, arr):
        arr.sort()
        # Case 1: Product of top 3 max elements
        case1 = arr[-1] * arr[-2] * arr[-3]
        # Case 2: Product of 2 smallest (most negative) and the largest
        case2 = arr[0] * arr[1] * arr[-1]
        return max(case1, case2)  # Return the maximum of both cases 
