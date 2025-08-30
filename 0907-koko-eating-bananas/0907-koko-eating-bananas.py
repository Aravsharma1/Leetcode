class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Key Idea: 

        '''
        Key Idea: 
        - the maximum value of k is the maximum value of piles. 
            for ex: if k is 12 (greater than max value of piles), thats the same 
            as having k as 11. So if k is 12, it would take 1 hour each for each pile
        - so the value of k is constrained between 1 and max(piles)
        - then in your main loop (don't have to check all the values of piles), check if 
        that value is a possible value of k
        - to check if that value is a possible value of k we can use a separate helper function
        - 
        '''
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
