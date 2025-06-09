class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force Solution:
        '''
        max_area = 0 
        for x in range(len(height)):
            for y in range(len(height)):
                if (x != y):
                    current_area = abs(x - y) * min(height[x], height[y])
                    if current_area > max_area:
                        max_area = current_area
        return max_area
        '''
        max_area = 0
        left = 0
        right = len(height) - 1
        while(left < right):
            current_area = abs(left - right) * min(height[left], height[right])
            if current_area > max_area:
                max_area = current_area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
