class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        # find k:
        k = 0 
        for x in range(0, len(nums)):
            if nums[x] != val:
                k += 1
        end = len(nums) - 1
        for start in range(0, k):
            while (nums[end] == val):
                    end -= 1
            if (nums[start] == val) and (start <= k):
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
            else: 
                start += 1
        return k
        
