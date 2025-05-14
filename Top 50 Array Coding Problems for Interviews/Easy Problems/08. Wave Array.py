from typing import List
class Solution:
    def convertToWave(self, arr : List[int]) -> None:
        # code here
        arr.sort()

        for i in range(0, len(arr)-1,2):
            arr[i], arr[i+1] = arr[i+1] , arr[i]
        return arr
