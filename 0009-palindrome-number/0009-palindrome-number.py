class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        reverse_number = 0
        duplicate = x
        while (x > 0):
            reverse_number = (10 * reverse_number) + (x % 10)
            x = x // 10
        
        return duplicate == reverse_number
        
        