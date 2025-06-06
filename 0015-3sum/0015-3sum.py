class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # extremely inefficient solution:
        # list_array = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if((i != j) and (i != k) and (j != k) and (nums[i] + nums[j] + nums[k] == 0) and ([nums[i], nums[j], nums[k]] not in list_array)):
        #                 list_array.append([nums[i], nums[j], nums[k]])
        # return list_array

        # efficient/better approach: 

    # Actual Approach: 

    # Sort the array 
        nums.sort()
        hashset = set()
        final_answer = []
        for i in range(len(nums)):
            j = i + 1  # or not j = 0 to make sure that the same numbers don't get checked again and again.
            k = len(nums) - 1
            while(j < k):
                current_sum = nums[i] + nums[j] + nums[k]
                if(i == j):
                    j += 1
                elif (i == k):
                    k -= 1
                elif(current_sum < 0):
                    j += 1
                elif(current_sum > 0):
                    k -= 1
                elif(current_sum == 0):
                    candidate = [nums[i], nums[j], nums[k]]
                    candidate.sort() # doing this so that we can make sure 
                    # that even for example if we have two triplets which have the same 
                    # element but in different order dont get added twice to final_answer
                    # so sorting them prevents two lists of same elements from being added
                    # to each other.
                    tuple_convert = tuple(candidate)
                    if tuple_convert not in hashset:
                        final_answer.append(candidate)
                        hashset.add(tuple_convert)
                    # use hashset to check if candidate for duplicate before adding to final_answer. 
                    # tuple: its immutable and you can only have immutable objects in hashsets and python, and so can't directly add candidate array directly because array/lists 
                    # are mutable objects. 
                    # using hashset is more efficient, look up in hashset: O(1) whereas lookup in array is O(n), so with hashset its O(n^2) and without it (with array): O(n)
                    j += 1
                    k -= 1
                    # j += 1, k -= 1 need to be done because once candidate has been found 
                    # then for that i we dont consider any other combinations and the earlier break statement instead of these 2 lines above would have done that because of which all combinations would not be considered, so instead we should keep considering all combinations until the j < k condition is being satisfied. 
        return final_answer

        

    
                    