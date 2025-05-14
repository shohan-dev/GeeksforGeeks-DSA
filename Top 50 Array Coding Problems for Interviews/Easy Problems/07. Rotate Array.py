class Solution:
    def rotateArr(self, arr, k):
        k = k % len(arr)
        rotated = arr[k:] + arr[:k]
        for i in range(len(arr)):
            arr[i] = rotated[i]  # write back into arr only for the main arr to update
