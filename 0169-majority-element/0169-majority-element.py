from collections import defaultdict
class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        counters = defaultdict(int)  # Default value for non-existing keys is 0

        # Count occurrences of each element
        for x in nums:
            
            counters[x] += 1  # No need to check if the key exists
        
        # Find the element that appears more than len(nums) // 2 times
        for key, value in counters.items():
            if value > len(nums) // 2:
                return key
