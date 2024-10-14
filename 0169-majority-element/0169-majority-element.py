from collections import defaultdict
class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        counters = defaultdict(int)  # Default value for non-existing keys is 0

        # Count occurrences of each element
        for x in nums:
            if x in counters:
                counters[x] += 1  # Increment count if the key exists
            else:
                counters[x] = 1   # Initialize key with value 1 if it doesn't exist

        
        # Find the element that appears more than len(nums) // 2 times
        for key, value in counters.items():
            if value > len(nums) // 2:
                return key
