class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        counter = 0
        # Step 1: fill nums1 up with nums2
        for x in range(m, len(nums1)):
            nums1[x] = nums2[counter]
            counter += 1
        # sort filled up nums1 using Python's sort() function. 
        nums1.sort()
