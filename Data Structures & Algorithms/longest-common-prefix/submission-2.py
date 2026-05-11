class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(0,len(sorted(strs)[0])):
            if sorted(strs)[0][i] == sorted(strs)[-1][i]:
                res.append(strs[0][i])
            else:
                break
        return(''.join(res))


            
        