class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_counter = {}
        left = 0
        right = 0
        max_freq = 0
        longest = 0

        while right < len(s):
            char = s[right]
            if char in freq_counter:
                freq_counter[char]+=1
            else:
                freq_counter[char] = 1
            max_freq = max(freq_counter[char] , max_freq)
            
            while right - left + 1 - max_freq > k:
                freq_counter[s[left]] = freq_counter[s[left]]  - 1
                left = left + 1
            longest = max(longest, right - left + 1)
            right = right + 1
        return longest


            


        