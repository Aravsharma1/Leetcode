class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        k = 0
        if(len(nums) <= 1):
            return len(nums)
        new_nums = [0] * len(nums)
        while(p2 < len(nums)):
            if ((nums[p2] == nums[p1]) and (p1 == p2)):
                new_nums[k] = nums[p2]
                p2 += 1
                k += 1
            elif ((nums[p1] != nums[p2]) and (p1 != p2)):
                p1 = p2
            else:
                p2 += 1
        for x in range(0, k):
            nums[x] = new_nums[x]
        return k