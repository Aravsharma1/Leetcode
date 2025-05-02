class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        new_length = 2*length
        ans = [0]* new_length
        counter = 0
        for i in range(0, new_length):
            ans[i] = nums[counter]
            counter += 1
            if(counter == length):
                counter = 0
        return ans
        