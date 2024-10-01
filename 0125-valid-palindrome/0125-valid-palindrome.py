class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        d = s.lower()
        start = 0
        end = length - 1
        while(start < end):
            if not(d[start].isalnum()):
                start += 1
            elif not(d[end].isalnum()):
                end -= 1
            elif d[start] != d[end]:
                return False
            else:
                start += 1
                end -= 1
        return True    