class Solution:
    def compress(self, chars: List[str]) -> int:
        
        count = 1
        j = 0
        for i in range(0,len(chars)):
            if i == len(chars)-1 or  chars[i+1]!=chars[i]:
                chars[j] = chars[i]
                j = j+1
                if count > 1:
                    for c in str(count):
                        chars[j] = c
                        j+=1
                count = 1 

                
            else:
                count+=1
        return j
        
        

