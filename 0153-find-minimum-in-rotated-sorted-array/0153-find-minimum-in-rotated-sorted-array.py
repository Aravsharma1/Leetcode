class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the critical point where you go from increasing 
        # to decreasing. 
        left = 0
        right = len(nums) -  1
        while(left < right):
            middle = (left + right) // 2 
            if nums[middle] > nums[right]:
                # do something
                left = middle + 1 # + 1 is important
            else: 
                # do something
                right = middle
        return nums[left]