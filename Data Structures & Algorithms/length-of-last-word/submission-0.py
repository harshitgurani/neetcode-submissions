class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        for word in l[::-1]:
            if word != '':
                return len(word)
        
