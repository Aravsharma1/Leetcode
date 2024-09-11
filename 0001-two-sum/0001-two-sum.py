class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [0,0]
        length = len(nums)
        for x in range(0,length):
            for y in range(x+1, length):
                if (nums[x] + nums[y]) == target:
                    arr[0] = x
                    arr[1] = y
                    return arr
                
        