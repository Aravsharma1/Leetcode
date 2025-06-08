class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        hashset = set()
        final_answer = []
        # for a in range(len(nums)):
        #     b = a + 1
        #     d = len(nums) - 1 
        #     while(b < d):
        #         if(current_sum > target):
        #             d -= 1
        #         elif (current_sum < target):
                    
        #         c = b + 1
        #         while(c < d):
        #             current_sum = nums[a] + nums[b] + nums[c] + nums[d]
        #             if current_sum == target: 
        #                 candidate = [nums[a], nums[b], nums[c], nums[d]]
        #                 candidate.sort() # for duplicate stuff 
        #                 candidate_tuple = tuple(candidate)
        #                 if (candidate_tuple not in hashset):
        #                     final_answer.append(candidate)
        #                     hashset.add(candidate_tuple)
        #             c += 1

        #new approach: 
        # use a 2 pointer approach , set a and b with double loop then c and d just need 
        # to find target - nums[a] - nums[b] : vague explanation of approach 
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                c = b + 1
                d = len(nums) - 1
                while(c < d):
                    if (nums[c] + nums[d] < target - nums[a] - nums[b]):
                        c += 1
                    elif (nums[c] + nums[d] > target - nums[a] - nums[b]):
                        d -= 1
                    else: 
                        # they are equal. 
                        candidate = [nums[a], nums[b], nums[c], nums[d]]
                        candidate_tuple = tuple(candidate)
                        if candidate_tuple not in hashset:
                            final_answer.append(candidate)
                            hashset.add(candidate_tuple)
                        c += 1 # important, don't forget!
                        d -= 1
        return final_answer


                    