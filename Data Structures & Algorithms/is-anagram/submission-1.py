class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for alphabet in s:
            if  alphabet in freq:
                freq[alphabet] += 1
            else:
                freq[alphabet] = 1
        for alphabet in t:
            if  alphabet not in freq:
                return False
            else:
                freq[alphabet] -= 1
        for alphabets in freq:
            if freq[alphabets] > 0:
                return False
        return True

        