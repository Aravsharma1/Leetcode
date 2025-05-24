class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        counter = 0
        for x in range(m, len(nums1)):
            nums1[x] = nums2[counter]
            counter += 1
        nums1.sort()
