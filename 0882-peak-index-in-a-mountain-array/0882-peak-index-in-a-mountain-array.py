class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr) - 1
        while (left < right):
            midpoint = (left + right)//2
            if arr[midpoint] < arr[midpoint + 1]:
                left = midpoint + 1
            else:
                right = midpoint
        return left