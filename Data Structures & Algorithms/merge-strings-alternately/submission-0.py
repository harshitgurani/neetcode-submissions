class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        a = min(len(word1),len(word2))
        for i in range(a):
            res.append(word1[i])
            res.append(word2[i])
        if len(word1) > len(word2): 
            final = ''.join(res) + word1[a:]
        else:
            final = ''.join(res) + word2[a:]
        return final

