class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # create a copy of nums 
        copy_nums = [0] * len(nums)
        for x in range(len(nums)):
            copy_nums[x] = nums[x]
        new_k = 0 # initializing, gets updated below. 
        if k >= len(nums):
            new_k = (k % len(nums))
        else:
            new_k = k
        special_case_counter = 0
        for x in range(len(nums)):
            if len(nums) - x <= new_k:
                # start from 0
                nums[special_case_counter] = copy_nums[x]
                special_case_counter += 1
            else:
                nums[x + new_k] = copy_nums[x]

         