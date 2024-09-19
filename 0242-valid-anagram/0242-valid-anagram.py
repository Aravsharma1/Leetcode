class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        # building the hashmap where the key is a char in s and t 
        # and the value is the number of occurences in s, t respectively 

        hashS, hashT = {}, {} # initializes 2 hashmaps 
        for x in range(len(s)):
            hashS[s[x]] = 1 + hashS.get(s[x], 0)
            hashT[t[x]] = 1 + hashT.get(t[x], 0)
        for c in hashS:
            # looping through hashS only, since hashS and hashT must be of the 
            # same length till now 
            if hashS[c] != hashT.get(c, 0):
                return False
        return True


        
        