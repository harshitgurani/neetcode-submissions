class Solution:
    def isPalindrome(self, s: str) -> bool:
        left , right = 0,len(s)-1
        while left < right :
            if s[left].isalnum() == False:
                left = left+1
                continue
            if s[right].isalnum() == False:
                right = right - 1
                continue
            if s[left].lower()!=s[right].lower():
                return False

            left = left +1
            right = right - 1
        return True


        