class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        is_palindrome = True
        while(left <= right):
            # check if elements are of alpanumeric type 
            # then if of alphanumeric type checks if they are alphabet and if yes convert that to lowercase. 
            # then compare regardless and update bool variable 
            if((s[left].isalnum()) and (s[right].isalnum())):
                if(s[left].isalpha() and s[right].isalpha()):
                    temp_left = s[left].lower()
                    temp_right = s[right].lower()
                    if temp_left == temp_right:
                        left += 1
                        right -= 1
                        is_palindrome = True
                    else:
                        return False
                else:
                    if (s[left] == s[right]):
                        left += 1
                        right -= 1
                        is_palindrome = True
                    else:
                        return False
            elif (not (s[left].isalnum())):
                left += 1
            elif (not (s[right].isalnum())):
                right -= 1
        return is_palindrome
