class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        # simple binary search implementation: O(log n) solution
        while(low <= high):
            mid = (low + high) // 2 #integer divison, not float divison 
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low