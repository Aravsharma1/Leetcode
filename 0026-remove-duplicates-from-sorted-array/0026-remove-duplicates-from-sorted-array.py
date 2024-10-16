class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if 0 == len(nums):
            return 0

        # Step 1: Find k 
        p1 = 0
        k = 1  
        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                k += 1
                p1 += 1
                nums[p1] = nums[p2]

        return k
