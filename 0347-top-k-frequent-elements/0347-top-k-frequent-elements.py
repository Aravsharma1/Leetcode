class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: creating a hashmap where the keys are each of the elements in
        # the array and values are the number of times these elements appear in the array
        countElements = {}
        for x in nums:
            if x in countElements:
                countElements[x] += 1
            else:
                countElements[x] = 1
        values_array = (len(countElements)) * [0]
        #key technique: can keep track of length of dictionary using len function (like for python)
        counter = 0
        for x in countElements:
            values_array[counter] = countElements[x]
            counter += 1
        values_array.sort()
        final_array = [0] * k
        copy_k = k 
        counter = 0
        used_keys = set()
        while(copy_k > 0):
            for key,value in countElements.items():
                if key in used_keys:
                    continue
                if values_array[-copy_k] == value:
                    final_array[counter] = key
                    counter += 1
                    copy_k -= 1
                    used_keys.add(key)
                    break  
        return final_array

