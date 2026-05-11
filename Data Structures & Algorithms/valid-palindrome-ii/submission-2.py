class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        left ,right = 0 , len(s)-1
        while left < right:
            if s[left]==s[right]:
                left=left+1
                right = right-1
            else:
                left = left + 1
                a = is_palindrome(left , right)
                left = left - 1
                right = right - 1
                b = is_palindrome(left , right)
                right = right + 1
                res = a or b
                return res
        return True





            



            



        