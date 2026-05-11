class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        longest_substring = 0 
        while right<len(s):
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1

            seen.add(s[right])
            substring  = right - left + 1
            longest_substring = max(substring,longest_substring)
            right+=1
        return longest_substring




        