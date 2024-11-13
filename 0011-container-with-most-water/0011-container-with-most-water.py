class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left = 0
        # right = len(height) - 1
        # maxarea = 1
        # while (left < right):
        #     current_area = (right - left) * min(height[left], height[right])
        #     if current_area > maxarea:
        #         maxarea = current_area
        #         left += 1
        #         right -= 1
        #     else:
        #         left += 1
        #         right -= 1
        # return maxarea

        #brute force O(n^2) solution: 
        # maxarea = 0
        # for x in range(len(height)):
        #     for y in range(len(height)):
        #         current_area = abs(y - x) * min(height[x], height[y])
        #         if current_area > maxarea:
        #             maxarea = current_area    
        # return maxarea
        # reattempting optimal solution: 
        maxarea = 0
        left = 0
        right = len(height) - 1
        while (left < right):
            current_area = min(height[left], height[right]) * abs(left - right)
            maxarea = max(current_area, maxarea)
            if height[left] > height[right]:
                right -= 1
            elif height[left] <= height[right]:
                left += 1
        return maxarea