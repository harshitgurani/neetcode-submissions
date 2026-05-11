class Solution:
    def maxDifference(self, s: str) -> int:

        freq = {}
        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
        odd_f=0
        even_f = 100
        for frequency in freq.values():
            if frequency%2==1:
                if frequency>odd_f:
                    odd_f = frequency
            else:
                if frequency<even_f:
                    even_f = frequency
        return(odd_f-even_f)


        