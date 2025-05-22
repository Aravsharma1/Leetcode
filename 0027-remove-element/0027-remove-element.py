class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter_k = 0
        dict_counter = 0
        dictionary = {}
        for x in range(len(nums)):
            if nums[x] != val:
                counter_k += 1
                dictionary[dict_counter] = nums[x]
                dict_counter += 1
        # dict has all of the values from nums not equal to value
        copy_counter_k = 0 # to not loose track of counter_k
        while(counter_k != copy_counter_k):
            nums[copy_counter_k] = dictionary[copy_counter_k]
            copy_counter_k += 1          
        return counter_k
        