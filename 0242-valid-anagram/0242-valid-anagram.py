class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        # keep count of each type of char in s
        # then check if every char in t appears the same amount of 
        # times as in s 
        # store it in a dictionary 
        dict_a = {}
        dict_b = {}
        for x in range(len(s)):
            if s[x] in dict_a:
                dict_a[s[x]] += 1
            else:
                dict_a[s[x]] = 1
        for x in range(len(t)):
            if t[x] in dict_b:
                dict_b[t[x]] += 1
            else:
                dict_b[t[x]] = 1
        for x in range(len(t)):
            if t[x] in dict_a:
                if(dict_b[t[x]] == dict_a[t[x]]):
                    continue
                else:
                    return False
            else:
                return False
        return True
