class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left_arr = [0]*length
        right_arr = [0]*length
        answer = [0]*length

        left_arr[0] = 1
        right_arr[length - 1] = 1

        for i in range(1,length):
            left_arr[i] = left_arr[i-1] * nums[i-1]
        for i in range(length - 2, -1, -1):
            right_arr[i] = right_arr[i + 1]* nums[i + 1]    
        
        for i in range(length):
            answer[i] = left_arr[i] * right_arr[i]
       # print(right_arr)    
        return answer