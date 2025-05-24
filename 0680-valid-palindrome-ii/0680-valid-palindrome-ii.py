class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 
        constraint = 1  # at most one deletion allowed

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if constraint == 0:
                    return False
                # Try skipping either the left or the right character
                # Check if the rest of the string is a palindrome after skipping one
                skip_left = True
                i, j = left + 1, right
                while i < j:
                    if s[i] != s[j]:
                        skip_left = False
                        break
                    i += 1
                    j -= 1

                skip_right = True
                i, j = left, right - 1
                while i < j:
                    if s[i] != s[j]:
                        skip_right = False
                        break
                    i += 1
                    j -= 1

                return skip_left or skip_right
        return True
