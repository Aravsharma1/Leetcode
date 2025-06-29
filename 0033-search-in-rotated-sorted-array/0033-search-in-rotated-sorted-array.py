class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # trivial O(n) solution:
        '''
        for x in range(len(nums)):
            if nums[x] == target: 
                return x
        return -1
        '''
        # actual O(log n) solution: 
        
        # step 1: find k first 
        # k = 0
        # for x in range(len(nums) - 1):

        #     if nums[x + 1] < nums[x]: 
        #         break
        #     else:
        #         k += 1
        # print(k)
        # # step 2: assuming we have k
        # left = k
        # right = k + 1
        # if (len(nums) == 1):
        #     if nums[0] == target:
        #         return 0
        #     else:
        #         return -1
        # while (left >= 0 or right <= len(nums) - 1):
        #     midpoint = (left + right) // 2
        #     if nums[midpoint] == target: 
        #         return midpoint
        #     elif nums[midpoint] > target: 
        #         right += 1
        #     else:
        #         left -= 1
        # return -1

        # new approach (not trolling):
        '''
        nums = [0,1,2,4,5,6,7]
        k = 2, n = [2,4,5,6,7,0,1]
        t = 0, output = 5

        k = 3, n = [4,5,6,7,0,1,2]
        t = 0, output = 4
        '''

        # Approach: use binary search to find the pivot index (index of the min_element). 
        # then based on this index, separate the array into 2 sub arrays. 
        # then based on target value and the index found search the corresponding sub array.

        # finding the minimum 
        left = 0
        right = len(nums) - 1
        while(left < right):
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        # left points to the minimum number
        if nums[left] == target:
            return left
        else:
            # 2 binary searches
            left_1 = 0
            right_1 = left - 1
            left_2 = left
            right_2 = len(nums) - 1
            while(left_1 <= right_1):
                mid = (left_1 + right_1) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left_1 += 1
                else:
                    right_1 -= 1
            while(left_2 <= right_2):
                mid = (left_2 + right_2) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left_2 += 1
                else:
                    right_2 -= 1
            return -1
            


