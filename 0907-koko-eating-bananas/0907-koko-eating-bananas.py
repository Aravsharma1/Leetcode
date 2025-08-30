class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Key Idea: 
        def check_k(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h

        # main function/logic 

        l = 1
        r = max(piles)
        # not really a binary search, we keep searching piles (efficiently, not all items are searched)
        while(l < r): # must not be l <= r, we stop when l = r
            k = (l + r) // 2
            if check_k(k):
                r = k
            else:
                l = k + 1
        return r # can return l also
