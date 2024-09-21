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

        # Step 2: Sorting the keys based on their frequencies in descending order
        sorted_keys = sorted(countElements, key=lambda x: countElements[x],reverse=True)

        # Step 3: Return the first k elements in the sorted keys
        return list(sorted_keys[:k])
