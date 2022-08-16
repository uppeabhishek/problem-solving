class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        new_num = 0
        
        temp = x
        
        while temp:
            rem = temp % 10
            new_num = new_num * 10 + rem
            temp = temp // 10
                
        return x == new_num