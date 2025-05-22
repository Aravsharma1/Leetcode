class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        for x in range(len(nums)):
            if nums[x] in dictionary:
                dictionary[nums[x]] += 1
            else:
                dictionary[nums[x]] = 1
        # key algorithmic approach: looping through dictionary values using 
        # values() function 
        # values returns a list of values of the dictionary
        max_value = 0
        for x in dictionary.values():
            if x >= max_value:
                max_value = x
        # max_value is a value
        for x in dictionary:
            if max_value == dictionary[x]:
                return x


        