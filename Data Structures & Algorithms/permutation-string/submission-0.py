class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        freq_s1 = {}
        for char in s1:
            if char in freq_s1:
                freq_s1[char]+=1
            else:
                freq_s1[char]=1

        freq_s2 = {}
        left = 0
        right = 0
        for right in range(len(s2)):
            if s2[right] in freq_s2:
                freq_s2[s2[right]]+=1
            else:
                freq_s2[s2[right]]=1
            if right - left + 1 > len(s1):
                freq_s2[s2[left]]-=1
                if freq_s2[s2[left]] == 0:
                    del freq_s2[s2[left]]
                left = left + 1
            if freq_s1 == freq_s2:
                return True
        return False




        