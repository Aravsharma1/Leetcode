class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] #declaring an empty array 
        for x in range(2):
            for n in nums: 
                ans.append(n)
        return ans