class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 
        constraint = 2
        valid_palindrome = False
        while(left <= right):
            if(s[left] == s[right]):
                valid_palindrome = True
                left += 1
                right -= 1
            else:
                constraint -= 1
                if(constraint == 0):
                    return False
                else:
                    # check whether substring until right - 1 is a palindrome
                    # check whether substring from left + 1 until end is a 
                    # palindrome
                    start_right = right - 1 # check this
                    check_left = True
                    temp_left = left
                    while(temp_left <= start_right):
                        if (s[temp_left] != s[start_right]):
                            check_left = False
                        temp_left += 1
                        start_right -= 1
                    start_left = left + 1 
                    temp_right = right
                    check_right = True
                    while(start_left <= temp_right):
                        if (s[start_left] != s[temp_right]):
                            check_right = False
                        start_left += 1
                        temp_right -= 1
                    return check_right or check_left # do an early return 
                    # no need to exit and then check
        return valid_palindrome
                
                
