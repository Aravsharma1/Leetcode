class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # inefficient solution:
        # arr = [0,0]
        # length = len(nums)
        # for x in range(0,length):
        #     for y in range(x+1, length):
        #         if (nums[x] + nums[y]) == target:
        #             arr[0] = x
        #             arr[1] = y
        #             return arr
        # efficient solution: 
        # create a default dictionary 
        dictionary = {}
        for x in range(len(nums)):
            dictionary[nums[x]] = x
        
        for x in range(len(nums)):
            y = nums[x]
            element = target - y
            if element in dictionary and dictionary[element] != x:
                return x, dictionary[element]