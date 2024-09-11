class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        length = len(nums)

        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
        